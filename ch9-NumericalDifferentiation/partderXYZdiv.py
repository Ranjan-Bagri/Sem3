# calculating the divergence of v_x(x,y,z)i+v_y(x,y,z)j+v_z(x,y,z)k
from math import * 
from derivative import dfdx3

# v = vx i + vy j + vz k
def vx(pr,x):
    [y,z]=pr
    return z-x**2-y**2
def vy(pr,y):
    [z,x]=pr
    return z-x**2-y**2
def vz(pr,z):
    [x,y]=pr
    return z-x**2-y**2

tol=1.0e-6
x0,y0,z0=1,-1,1 # point of interest
dfdx_yz=dfdx3(vx,[y0,z0],x0,tol)
dfdy_zx=dfdx3(vy,[z0,x0],y0,tol)
dfdz_xy=dfdx3(vz,[x0,y0],z0,tol)
div=dfdx_yz+dfdy_zx+dfdz_xy
print(div)