# Riccati's eqn
import matplotlib.pyplot as plt 
from RK4_1d import RK4_1d

def f(a,x,y):
    return a*y**2-y*x**2+x
a=-1
x0,y0=0,1

xn,dx=-0.7,-0.01
xr,yr,dydx=RK4_1d(f,a,x0,y0,dx,xn)
xn,dx=5,0.01
xf,yf,dydx=RK4_1d(f,a,x0,y0,dx,xn)
plt.plot(xr,yr,'k--',label='reverse direction')
plt.plot(xf,yf,'k-',label='forward direction')
plt.title('Solving Riccati eqn with rk4')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()