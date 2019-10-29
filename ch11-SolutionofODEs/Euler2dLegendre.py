import numpy as np 
import matplotlib.pyplot as plt 
from Euler2d import Euler2d
import sys
sys.path.append('../ch12-SpecialFunctions/')
from legendre import recPn

def f(n,x,y,dydx):
    # function of legendre diff equ with n tunable from main
    return (2*x*dydx)/(1-x**2)-(n*(n+1)*y)/(1-x**2)
def dPndx(n,x):
    if n==0:
        drv=0
    else:
        drv=(n/(x**2-1))*(x*recPn(n,x)-recPn(n-1,x))
    return drv
n=4 # order of Legendre diff eqn
x=0.0 # initial values
y,dydx=recPn(n,x),dPndx(n,x)
# reverse order setting
dx,X=-0.001,-3.0
x1,y1,dydx1,d2ydx21=Euler2d(f,n,x,y,dydx,dx,X)
# forward order setting
dx,X=0.001,3.0
x2,y2,dydx2,d2ydx22=Euler2d(f,n,x,y,dydx,dx,X)
fig=plt.figure()
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)
ax1.plot(x1,y1,'k-',label='Calculated reverse') # plot in both direction with different style
ax1.plot(x2,y2,'k--',label='Calculated forward')
ax1.legend(loc='best',prop={'size':12})

xx=np.arange(-X,X,0.1) # numpy array of x for plotting
yy=recPn(n,xx) # exact Legendre function for n=3
ax2.plot(xx,yy,'k:',label='Exact')
ax2.legend(loc='best',prop={'size':12})

plt.xlabel('x')
plt.show()