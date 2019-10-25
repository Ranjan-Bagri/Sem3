# Calculating partial derivative using parameter of the function
from derivative import dfdx3

def fx(y,x):
    # pr -> y,x -> x
    return 2*x**2-x*y+y**2
def fy(x,y):
    # pr -> x,y -> y,
    return 2*x**2-x*y+y**2

tol=1.0e-6
x,y=1,2
dfdx_y=dfdx3(fx,y,x,tol)
dfdy_x=dfdx3(fy,x,y,tol)
print(dfdx_y,dfdy_x,'exact=',2,3)