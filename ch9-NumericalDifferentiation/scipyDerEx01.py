# Derivative using scipy.misc.derivative
# syntax : scipy.misc.derivative(func,x0,dx=1.0,n=1,args=(),order=3)
# arguments:
# func ==> user defined function , func(x,args()) , mandatory
# x0 ==> the point at which nth order derivative to be found, float, mandatory
# dx ==> step length, float, optional, default is dx=1.0
# n ==> order of derivative, integer, optional, default is n=1
# args ==> extra parameters to be passed to the user defined func, tuple, optional, defaul is blank tuple
# order ==> number of neighbourhod points is to be used, integer,optional, default is order =3
# returns:
# dfdx ==> nth order derivative of the user defined function at x0

from scipy.misc import derivative
from math import * 
import matplotlib.pyplot as plt 
def func(x):
    return sin(x**2)*exp(-x)
x,ypn=[],[] # x-array and y^n-array , y^n => nth order derivative
xStart=True # bollean variable to switch-off record of x-array after once
d=4
for n in range(1,5):
    m=2*n+1
    h=10**(-d/n)
    xx=-pi
    yp=[]
    while x<= pi:
        if xStart:
            x.append(xx)
        yp.append(derivative(func,xx,h,n=n,order=m))
        xx+=0.01
    ypn.append(yp)
    xStart=False # swithch-off record of x-array

for i in range(4):
    plt.plot(x,ypn[i],label=r'$f^%d(x)'%(i+1))
plt.legend(loc='best',prop={'size':12})
plt.show()