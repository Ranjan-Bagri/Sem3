from disToCnt import *
from math import *
import matplotlib.pyplot as plt 

#=====Creation of discrete function======
# Continuous function from which discrete function is created
def f(x):
    return exp(-0.15*x)*sin(2*x)

m=4 # number of local points
h,hh=0.3,0.06 # x-spacing of discrete function and interpolated function
x,fx=[],[] # array of discrete function
xx=-2*pi # initial x-value of discrete function
while xx<=2*pi: # final x-value
    x.append(xx)
    fx.append(f(xx))
    xx+=h

#=====Creation of 1st set of interpolated data=======
X1,Y1=[],[]
xx=-2*pi
while xx<=-1.1*pi:
    X1.append(xx)
    Y1.append(disToCnt(x,fx,xx,m))
    xx+=hh

#======Creation of 2nd set of interpolated data=======
X2,Y2=[],[]
xx=-0.9*pi
while xx<=-0.5*pi:
    X1.append(xx)
    Y1.append(disToCnt(x,fx,xx,m))
    xx+=hh

#======Creation of 3rd set of interpolated data=======
X3,Y3=[],[]
xx=pi
while xx<=1.5*pi:
    X1.append(xx)
    Y1.append(disToCnt(x,fx,xx,m))
    xx+=hh

#======Plot the data=====
plt.plot(X1,Y1,'c.',label=r'$-2\pi \leq x \leq -1.1\pi$')
plt.plot(X2,Y2,'c4',label=r'$-0.9\pi \leq x \leq 0.5\pi$')
plt.plot(X3,Y3,'cx',label=r'$\pi \leq x \leq 1.5\pi$')
plt.plot(x,fx,'k*',label='Discrete Fnc')
plt.legend(loc='best',prop={'size':12})
plt.title('Illustration of local interpolation')
plt.show()