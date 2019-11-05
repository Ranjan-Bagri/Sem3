# RK4 for solving nonlinear oscillator
import matplotlib.pyplot as plt 
from RK4_2d import RK4_2d

def f(eps,t,x,dxdt):
    return eps*(1-x**2)*dxdt-x 
Eps=[0.1,1.0,10.0] # values of epsilon
t0,x0,dxdt0=0,0,0.3 # initial conditions
dt=0.01

plt.suptitle(r'Solution of $\frac{d^2x}{dt^2}=\epsilon(1-x^2)\frac{dx}{dt}$')
tn=[100,30,50] # final times
for i in range(len(Eps)):
    t,x,dxdt,d2xdt2=RK4_2d(f,Eps[i],t0,x0,dxdt0,dt,tn[i])
    plt.subplot(3,1,i+1)
    plt.plot(t,x,'k',label=r'$\epsilon$=%.2f'%Eps[i])
    plt.legend(loc='best',prop={'size':12})
    plt.ylabel('x')
plt.xlabel('t')
plt.show()