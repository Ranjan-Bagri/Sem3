# Intrego differential equation
import numpy as np 
import matplotlib.pyplot as plt 
from Euler1d import Euler1d
import sys
sys.path.append('../ch10-NumericalIntegration/')
from simp13X import simp13X

def infc(pr,t):
    return np.exp(abs(pr-t))
def f(pr,x,y):
    ifx=simp13X(infc,x,0,x,1.0e-5) # parameter=x, limit=[0,x]
    return pr[0]*y+pr[1]*ifx
def ff(pr,x,y):
    return pr[0]*y+pr[1]*(np.exp(x)-1)

x,y=0.0,0.0 # initial values
pr=[-2,-5] # array of coefficients
dx,X=0.01,10
x1,y1,dydx1=Euler1d(f,pr,x,y,dx,X)
x2,y2,dydx2=Euler1d(ff,pr,x,y,dx,X)

plt.plot(x1,y1,'k',label=r'$f(x,y)=-2y-5\int_0^x e^{|x-t|}dt$')
plt.plot(x2,y2,'k.',markevery=6,label=r'$f(x,y)=-2y-5 (e^x-1)$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()