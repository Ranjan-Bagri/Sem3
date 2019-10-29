# This is the demonstration to attempt to obtain the solution in undefined regime
import matplotlib.pyplot as plt 
from Euler1d import Euler1d

def f(omg,x,y):
    return -omg**2*x/y
omg=3.0
x,y=0.0,omg # initial condition
# reverse direction -1<=x<=0
h,X=-0.0001,1.0
x1,y1,dydx1=Euler1d(f,omg,x,y,h,X)
# forward direction
h=0.0001
x2,y2,dydx2=Euler1d(f,omg,x,y,h,X)
# increse the limit X=1.02, X>1.0 is undefined
X=1.02
x3,y3,dydx3=Euler1d(f,omg,x,y,h,X)

fig=plt.figure()
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)
ax1.plot(x1,y1,'k',label=r'for $-1 \leq x \leq 0$')
ax1.plot(x2,y2,'k-',label=r'for $0 \leq x \leq 1$')
plt.legend(loc='best',prop={'size':12})
ax1.plot(x3,y3,'k:',label=r'for $0 \leq x \leq 1.02$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()