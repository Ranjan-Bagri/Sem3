# calculating directional derivative
from math import * 
from derivative import dfdx3 

def phix(pr,x):
    [y,z]=pr
    return x**2*y*z+4*x*z**2
def phiy(pr,y):
    [z,x]=pr
    return x**2*y*z+4*x*z**2
def phiz(pr,z):
    [x,y]=pr
    return x**2*y*z+4*x*z**2

tol=1.0e-6
x,y,z=1,-2,-1 # point of interest
dfdx_yz=dfdx3(phix,[y,z],x,tol)
dfdy_zx=dfdx3(phiy,[z,x],y,tol)
dfdz_xy=dfdx3(phiz,[x,y],z,tol)
gradPhi=[dfdx_yz,dfdy_zx,dfdz_xy]
print('grad phi=',gradPhi)
a=[2,-1,-2] # a vector
amod=0 # magnitude of 'a' vector
for i in a:
    amod+=i**2
amod=amod**0.5
ua=[a[i]/amod for i in range(len(a))]
print('Unit vector of a=',ua)
dirDrv=0
for i in range(len(a)):
    dirDrv+=gradPhi[i]*ua[i]
print('Directional derivative=',dirDrv)