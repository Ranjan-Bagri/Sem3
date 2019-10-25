# This is an example where y=f(x) can't be written but dy/dx is determined at (x0,y0) with the help of taylor's series expansion
# dy/dx  = (del phi(x,y)/del x)_y/(del phi(x,y)/del y)_x

from math import *
from derivative import dfdx3 
def phix(y,x):
    return y**2+2*x**2*y-3*x+2*y+5
def phiy(x,y):
    return y**2+2*x**2*y-3*x+2*y+5

tol=1.0e-6
x0,y0=1,3**0.5
dPhidx_y=dfdx3(phix,y0,x0,tol)
dPhidy_x=dfdx3(phiy,x0,y0,tol)
dydx=dPhidx_y/dPhidy_x
print(dydx)