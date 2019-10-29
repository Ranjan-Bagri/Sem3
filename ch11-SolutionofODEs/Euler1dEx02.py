# Demonstration of solution of a 1st order differential equation by Euler Method.
# This example to verify solution which is a function of both x and y

import matplotlib.pyplot as plt 
import numpy as np 
from Euler1d import Euler1d

# f(x,y) ==> (3x^2-2x)/(3y^2+1) 
# Exact result ==> y^3+3=x^3-x^2
# so plot of y^3+3 vs x^3-x^2 will be linear

def f(pr,x,y):
    return (3*x**2-2*x)/(3*y**2+1)

x,y=0.0,0.0 # initial values of x and y
h,X=0.01,50.0 # values of initial step length and final values of x
x,y,dydx=Euler1d(f,None,x,y,h,X) # x,y,dydx are arrays
x,y=np.asarray(x),np.asarray(y) # return list converted to numpy array
#plt.plot(x,y)
# Verification with the exact result. Solpe of this curve will be unity
plt.plot(x**3-x**2,y**3+y,'k',label=r'$y^3+y$ vs $x^3-x^2$')
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
plt.legend(loc='best',prop={'size':12})
plt.title(r'Solution of $\frac{dy}{dx}=\frac{3x^2-2x}{3y^2+1}$ by Euler Method')
plt.xlabel(r'$x^3-x^2$')
plt.ylabel(r'$y^3+3$')
plt.show()