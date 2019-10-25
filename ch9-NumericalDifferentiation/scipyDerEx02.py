from scipy.misc import derivative
from math import * 
import matplotlib.pyplot as plt 

def f(x):
    return x**2*sin(x)
h=1e-4
xx=-pi
x,y,dydx=[],[],[]
while xx <=pi:
    x.append(xx)
    y.append(f(xx))
    dydx.append(derivative(f,xx,h,n=1,order=3))
    xx+=0.01
plt.plot(x,y,'k:',label=r'y(x)')
plt.plot(x,dydx,'k',label=r'$\frac{dy}{dx}$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()