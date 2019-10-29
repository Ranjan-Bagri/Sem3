# Solution of Newton's law of motion
# d2x/dt2=a
import matplotlib.pyplot as plt 
from Euler2d import Euler2d

def f(a,t,x,dxdt):
    return a
a=1.0
t,x,dxdt=0.0,0.0,0.0 # initial conditions
dt,T=0.01,1.8 # value of T choosen arbitrarily
tt,xx,Adxdt,Ad2xdt2=Euler2d(f,a,t,x,dxdt,dt,T)
plt.plot(tt,xx,'k',label='a=%.2f'%a)
plt.title(r'solution of $\frac{d^2 x}{dt^2}=a$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('t')
plt.ylabel('x')
plt.show()