def f(x):
    return (x**2-1)**d
def fct(n):
    fc=1
    for i in range(1,n+1):
        fc*=i
    return fc

from scipy.misc import derivative
import matplotlib.pyplot as plt 
import numpy as np 
from legendre import recPn

d=3 # order of derivative/ legendre polynomial
m=2*d+1 # number of neighbourhood points
h=10**(-4/d) # increment

xx,yy,yy1=[],[],[]
x=-0.94
while x<=0.94:
    xx.append(x)
    yy.append(derivative(f,x,h,n=d,order=m)/(2**d*fct(d))) # Rodrigues
    yy1.append(recPn(d,x)) # exact
    x+=0.01

plt.plot(xx,yy1,'k',xx,yy,'k.',markevery=3)
plt.title('Verification of Rodrigues formula for n=%d'%d)
plt.legend(['exact','Rodrigues formula'],loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()