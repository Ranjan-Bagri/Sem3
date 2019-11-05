# Solving Bernoulli's equation
import numpy as np 
from RK4_1d import RK4_1d

def f(x):
    return 5
def g(x):
    return np.exp(-2*x)
def F(mu,x,y):
    return f(x)*y+g(x)*y**mu
mu=-2
x0,y0=0,2 # initial condition

# solution calculated with rk4
dx,X0=-0.01,-2.5
xr,yr,dydx=RK4_1d(F,mu,x0,y0,dx,X0) # reverse solution
dx,X1=0.01,0.5
xf,yf,dydx=RK4_1d(F,mu,x0,y0,dx,X0) # forward solution

import matplotlib.pyplot as plt 
plt.plot(xr,yr,'k--',label='reverse direction')
plt.plot(xf,yf,'k-',label='forward direction')
plt.title('Solving Bernoulli eqn with rk4')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()