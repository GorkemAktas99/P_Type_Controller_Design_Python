"""
    @author Görkem Aktaş
    @date 30.04.2021
    @brief This application shows that how to design a P type controller in Python
    In this case, I have chosen a sample system that is Gs = 1/(s*(s+5)*(s+8)).
    You can use familiar steps and realize P type controller for your system
    I have mentioned steps as comment.
"""
"""
    Firstly, we have to import sympy library. Sympy is same symbolic toolbox being in matlab.
    Then import control lib
"""
from sympy import *
import numpy as np
from control import *
import matplotlib.pyplot as plt
ts = 2.5 #Desired SettlingTime
s = Symbol('s')
Gss = 1/(s*(s+5)*(s+8))
wn = Symbol('wn')
zeta = 4/(ts*wn)
pds = s**2+2*zeta*wn*s+wn**2 #The ideal system's denumerator to be
p = Symbol('p')
pes = s+p #Residue Polynomial
ps = pds*pes
k = Symbol('k')
Tss = (k*Gss)/(1+k*Gss)
Tss = cancel(Tss)
n,d = fraction(Tss) #numden() function
print(d)
ps = collect(expand(ps),s)
print(ps)
d = Poly(d,s)
ps = Poly(ps,s)
d_den = d.coeffs()
ps_den = ps.coeffs()
print(d_den)
print(ps_den)
eq_list = [] #Equations list for solving
"""
    I have created a loop for taking equations from d_den and ps_den
"""
for i in range(1,len(d_den)):
    eq_list.append(Eq(d_den[i],ps_den[i]))
print(eq_list)
sol = nonlinsolve(eq_list,[p,wn,k]) #NonLinear Solution
print(sol)
solution_list = []
for i in sol:
    solution_list.append(i)
print(solution_list)
solutions = []
for i in range(3):
    solutions.append(solution_list[1][i])
print(solutions)
Fs = np.array(solutions[2],ndmin=1,dtype=np.dtype(float))

Gs = tf(1,[1,13,40,0])
print(Gs)
Ts = feedback(Gs*Fs,1)
print(Ts)
t,y = step_response(Ts)
plt.plot(t,y)
plt.grid()
plt.show()
