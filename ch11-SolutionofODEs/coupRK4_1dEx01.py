# Example of solving two coupled 1st order non-linear equations
from coupRK4_1d import coupRK_41d
import matplotlib.pyplot as plt 

def f(a,x,y,z):
    return z+y*((y**2+z**2)**0.5-2*a)
def g(a,x,y,z):
    return -y+z*((y**2+z**2)**0.5-2*a)
a=1
x0,y0,z0=0.05,1,0
xn,dx=5.0,0.01

x,[y,dydx],[z,dzdx]=coupRK_41d(f,g,a,a,x0,y0,z0,dx,xn)

plt.plot(x,y,'k',label='x vs y')
plt.plot(x,z,'k--',label='x vs z')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()