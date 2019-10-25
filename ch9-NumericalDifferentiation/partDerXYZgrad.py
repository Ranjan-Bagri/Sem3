# Determination of gradient and unit normal of a scalar field f(x,y,z) at user given point
from math import * 
from derivative import dfdx3 

def phix(pr,x):
    [y,z]=pr
    return log((x**2+y**2+z**2)**0.5)
def phiy(pr,y):
    [z,x]=pr
    return log((x**2+y**2+z**2)**0.5)
def phiz(pr,z):
    [x,y]=pr
    return log((x**2+y**2+z**2)**0.5)

tol=1.0e-6
x,y,z=0,-2,1
dfdx_yz=dfdx3(phix,[y,z],x,tol)
dfdy_zx=dfdx3(phiy,[z,x],y,tol)
dfdz_xy=dfdx3(phiz,[x,y],z,tol)
print('grad phi=',dfdx_yz,'i+',dfdy_zx,'j+',dfdz_xy,'k')
unrX=dfdx_yz/(dfdx_yz**2+dfdy_zx**2+dfdz_xy**2)**0.5
unrY=dfdy_zx/(dfdx_yz**2+dfdy_zx**2+dfdz_xy**2)**0.5
unrZ=dfdz_xy/(dfdx_yz**2+dfdy_zx**2+dfdz_xy**2)**0.5
print("Unit normal=",unrX,'i+',unrY,'j+',unrZ,'k')