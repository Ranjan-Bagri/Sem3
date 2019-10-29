# Obtain legendre polynomial from generating function
def LegdGen(t):
    # Generating function
    # x is the global variable
    return 1/(1-2*x*t+t**2)**0.5
def fct(n): # factorial
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
t=0.0
x=-0.94
while x<=0.94:
    xx.append(x)
    yy.append(derivative(LegdGen,t,h,n=d,order=m)/fct(d))
    yy1.append(recPn(d,x)) # exact
    x+=0.01

plt.plot(xx,yy1,'k',xx,yy,'k.',markevery=3)
plt.title('Legendre polynomial from generating function for n=%d'%d)
plt.legend(['exact','from generating function'],loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()