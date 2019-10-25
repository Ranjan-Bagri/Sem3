# Calculating the components of a scalar fields f(x,y,z)
from math import * 
from derivative import dfdx3

def fx(pr,x):
    [y,z]=pr
    return x**2*y-10*y**2*z**3+43*x-7*tan(4*y)
def fy(pr,y):
    [z,x]=pr
    return x**2*y-10*y**2*z**3+43*x-7*tan(4*y)
def fz(pr,z):
    [x,y]=pr
    return x**2*y-10*y**2*z**3+43*x-7*tan(4*y)
tol=1.0e-6
x,y,z=1,1,1
dfdx_yz=dfdx3(fx,[y,z],x,tol)
dfdy_zx=dfdx3(fy,[z,x],y,tol)
dfdz_xy=dfdx3(fz,[x,y],z,tol)
print(dfdx_yz,dfdy_zx,dfdz_xy)
print('exact=',2*x*y+43,x**2-20*y*z**3-28*(1/(cos(4*y))**2,-30*y**2*z**2))