# Comparison betwwen Euler method and RK4 method
import matplotlib.pyplot as plt 
import numpy as np 
from Euler1d import Euler1d
from RK4_1d import RK4_1d

def f(pr,x,y):
    return x**4*y
def exc(x): # exact solution
    return np.exp(x**5/5)/np.exp(1/5)
x0,y0=1,1.0 # initial condition
xn,dx=2.55,0.01
x,y,dydx=Euler1d(f,None,x0,y0,dx,xn) # solution by euler method
plt.plot(x,y,'k--',label='Euler method')

x,y,dydx=RK4_1d(f,None,x0,y0,dx,xn) # solution by rk4 method
plt.plot(x,y,'k',label='rk4 method')
x=np.asarray(x)
y=exc(x) # exact solution
plt.xlim(2.3,2.56)
plt.plot(x,y,'k.',markevery=1,label='Exact')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()