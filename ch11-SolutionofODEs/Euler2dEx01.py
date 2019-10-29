# demonstration of solving non-linear differential equation with varying initial conditions
#xy(d2y/dx2)=x(dy/dx)^2-y(dy/dx)
import numpy as np 
import matplotlib.pyplot as plt 
from Euler2d import Euler2d

def f(pr,x,y,dydx):
    return dydx**2/y-dydx/x
lnst=['k-','k--','k-.','k:'] # array of line styles
dx,X=0.01,10.0
# numpy array for plotting exact result
xx=np.arange(1.0,10.2,0.5)
# starting values of parameters
a,b,i=1.0,-2.0,0
while b<2.0:
    # below initial conditions changing with parameter a,b
    x,y,dydx=1.0,a,a*b
    x,y,dydx,d2ydx2=Euler2d(f,None,x,y,dydx,dx,X)
    lb='calculated for b=%.2f'%b
    plt.plot(x,y,lnst[i],label=lb)
    # plot of exact solution
    plt.plot(xx,a*xx**b,'k.',label='exact')
    plt.title('Solution of ODE for varying initial conditions')
    plt.legend(loc='best',prop={'size':12})
    plt.xlabel('x')
    plt.ylabel('y')
    b+=1.0
    i+=1
plt.show()
