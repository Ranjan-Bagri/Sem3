from imEuler1d import imEuler1d
import matplotlib.pyplot as plt 
import numpy as np 
from Euler1d import Euler1d

def f(pr,x,y):
    return 0.5*y


dx,X=0.1,20.0 # values of initial step length and final values of x
x,y=0.0,10.0 # initial values of x and y
x,y,dydx=imEuler1d(f,None,x,y,dx,X)
plt.plot(x,y,'k-',label='Improved euler method')
x,y=0.0,10.0 # initial values of x and y
x,y,dydx=Euler1d(f,None,x,y,dx,X)
plt.plot(x,y,'k-.',label='simple euler method')
x=np.arange(0.0,X,1.0) 
plt.plot(x,10.0*np.exp(x/2),'k*',label='Exact Solution')
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.title('Demonstration of improved and simple Euler methods')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()