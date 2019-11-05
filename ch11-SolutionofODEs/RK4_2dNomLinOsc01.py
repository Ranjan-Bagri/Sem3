# Solving equation corresponding to non-linear oscillator
import numpy as np 
import matplotlib.pyplot as plt 
from RK4_2d import RK4_2d

def f(pr,t,x,dxdt):
    a,b,gm,om=pr
    return gm*np.cos(om*t)-a*x-b*x**3
a,gm,om=2,2.0,1.0 # coefficient of equation
t0,x0,dxdt0=0,1.0,0.0 # initial conditions
T,dt=3*2*np.pi/om,0.01 # final value of time and increment
b=[0,0.1,5.6] # coefficients of nonlinear terms
n=len(b)
for i in range(n):
    pr=[a,b[i],gm,om]
    t,x,dxdt,d2xdt2=RK4_2d(f,pr,t0,x0,dxdt0,dt,T) # solution
    plt.subplot(n,1,i+1)
    plt.plot(t,x,'k',label='b=%.3f'%b[i])
    plt.legend(loc='best',prop={'size':12})
plt.suptitle(r'$\frac{d^2x}{dt^2}+ax+bx^3 = \Gamma \cos \omega t$')
plt.xlabel('t')
plt.show()