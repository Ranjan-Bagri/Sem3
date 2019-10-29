import matplotlib.pyplot as plt 
import numpy as np 
from Euler1d import Euler1d

def f(pr,x,y):
    return 2*y

x,y=0.0,5.0 # initial values of x and y
h,X=0.005,10.0 # values of initial step length and final values of x
x,y,dydx=Euler1d(f,None,x,y,h,X)
plt.plot(x,y,'k',label='Solution by euler method')
xx=np.arange(0.0,10.0,0.01) 
plt.plot(xx,5.0*np.exp(2*xx),'k--',label='Exact Solution')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Solution of $\frac{dy}{dx}=2y$ by Euler Method')
plt.show()
