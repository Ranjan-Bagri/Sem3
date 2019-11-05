# Demonstration of maximum and minimum of a function
import numpy as np 
import matplotlib.pyplot as plt 
from derivative import dfdx3
import sys
sys.path.append("../ch8-RootFinding/")
from bisec import bisec

tol=1.0e-6 # tolerence of calculation
def f(pr,x):
    # function of which max/min is to be determined
    # parameter set to None from main
    return (x**2)*np.exp(-x**2)

def fprime(pr,x):
    # df/dx
    # parameter set to None from main
    return dfdx3(f,pr,x,tol)
x1,x2=0.5,5.0 # range of calculation of max/min
xs=bisec(fprime,None,x1,x2,tol) # solution of df/dx=0
print("x-value at max/min=",xs) # solution
xx,fx,dfdx=[],[],[] # arrays for plotting
x=x1
while x<=x2:
    xx.append(x)
    fx.append(f(None,x))
    dfdx.append(fprime(None,x))
    x+=0.1
xax=[0.0 for i in range(len(xx))] # x-axis
plt.plot(xx,fx,'k',label='f(x)')
plt.plot(xx,dfdx,'k--',label=r'$\frac{df}{dx}$')
plt.plot(xx,xax,'k:',label='x-axis')
plt.plot(xs,f(None,xs),'k.',label=r'$(x_0,f(x_0))$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.title('Demonstration of maxima and minima of a function')
plt.show()