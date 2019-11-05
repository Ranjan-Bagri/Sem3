# Displacement and phase-space corresponding to Vander Pol oscillator
import numpy as np 
from RK4_2d import RK4_2d

def f(mu,t,x,dxdt):
    return mu*(1-x**2)*dxdt-x

t0,x0,dxdt0=0,0,1
dt=0.01

import matplotlib.pyplot as plt 
T=50
mu=0.2
t,x,dxdt,d2xdt2=RK4_2d(f,mu,t0,x0,dxdt0,dt,T)
plt.plot(t,x,'k')
plt.ylim(-4,4)
plt.xlabel('t')
plt.ylabel('x')
plt.title('Displacement of Vander Pol oscillator')
plt.show()
T=9
plt.axis('equal')
while mu<=4.0:
    t,x,dxdt,d2xdt2=RK4_2d(f,mu,t0,x0,dxdt0,dt,T)
    mu+=0.4
    plt.plot(x,dxdt,label=r'$\mu=%.2f$'%mu)
    plt.legend(loc='best',prop={'size':12})
    plt.xlabel('x')
    plt.ylabel(r'$\frac{dx}{dt}$')
    plt.title('Phase space for Vander Pol oscillator')
plt.show()