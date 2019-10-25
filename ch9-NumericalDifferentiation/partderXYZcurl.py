# calculating the curl of vx(x,y,z)i+vy(x,y,z)j+vz(x,y,z)k
from math import * 
from derivative import dfdx3 

# v = vx i + vy j + vz k
def Vx_y(pr,y):
    [z,x]=pr
    return x*z**3 #vx
def Vx_z(pr,z):
    [x,y]=pr
    return x*z**3 # vx
def Vy_z(pr,z):
    [x,y]=pr
    return -2*x**2*y*z # vy
def Vy_x(pr,x):
    [y,z]=pr
    return -2*x**2*y*z # vy
def Vz_x(pr,x):
    [y,z]=pr
    return 2*y*z**4 # vz
def Vz_y(pr,y):
    [z,x]=pr
    return 2*y*z**4 # vz
tol=1.0e-6
x0,y0,z0=1,-1,1
dVxdy=dfdx3(Vx_y,[z0,x0],y0,tol)
dVxdz=dfdx3(Vx_z,[x0,y0],z0,tol)
dVydz=dfdx3(Vy_z,[x0,y0],z0,tol)
dVydx=dfdx3(Vy_x,[y0,z0],x0,tol)
dVzdx=dfdx3(Vz_x,[y0,z0],x0,tol)
dVzdy=dfdx3(Vz_y,[z0,x0],y0,tol)

curl=[dVzdy-dVydz,dVxdz-dVzdx,dVydx-dVxdy]
print(curl)