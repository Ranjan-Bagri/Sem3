# Solution of Bessel differential equation by Euler method
import numpy as np 
import matplotlib.pyplot as plt 
from Euler2d import Euler2d
import scipy.special as ss 

def f(n,x,y,dydx):
    # function of bessel diff eqn with n tunable from main
    return -dydx/x-(1-n**2/x**2)*y
n=3 # order of bessel function
dx,X=0.01,20.0
# initial conditions
x=0.5
y,dydx=ss.jv(n,x),ss.jvp(n,x) # Jn(0.5) and jn'(0.5) taken from scipy
xx=np.arange(x,X,dx*20) # numpy array to compare
yy=ss.jv(n,xx) # bessel functions from scipy
# result from euler method
x,y,dydx,d2ydx2=Euler2d(f,n,x,y,dydx,dx,X)
plt.plot(x,y,'k-',label='exact')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
tl='solution of Bessel differential equation for n=%d'%n
plt.title(tl)
plt.show()