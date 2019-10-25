import matplotlib as mpl 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np 
from derivative import dfdx3

def fx(y,x):
    return x**3*y+np.exp(x*y**2)
def fy(x,y):
    return x**3*y+np.exp(x*y**2)

tol=1.0e-6
x0,y0,xn,yn=0.1,0.1,1.0,1.0
dx,dy=0.05,0.05
xx,yy,dfdx_y,dfdy_x,dfdx_yy,dfdy_xx=[],[],[],[],[],[]
y=y0
while y<=yn:
    x=x0
    while x<=xn:
        xx.append(x)
        yy.append(y)
        dfdx_y.append(dfdx3(fx,y,x,tol))
        dfdy_x.append(dfdx3(fy,x,y,tol))
        dfdx_yy.append(3*x**2*y+y**2*np.exp(x*y**2))
        dfdy_xx.append(x**3+2*x*y*np.exp(x*y**2))
        x+=dx
    y+=dy

fig=plt.figure()
ax=fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel(r'$\frac{\partial f}{\partial x}$')
ax.plot(xx,yy,dfdx_y,'bx')
ax.plot(xx,yy,dfdx_yy,'k.')
plt.show()
fig=plt.figure()
ax=fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel(r'$\frac{\partial f}{\partial y}$')
ax.plot(xx,yy,dfdy_x,'bx')
ax.plot(xx,yy,dfdy_xx,'k.')
plt.show()
