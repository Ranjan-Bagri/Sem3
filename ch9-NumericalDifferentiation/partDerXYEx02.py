# Calculating partial derivative using parameter of the function
from derivative import dfdx3

def fx(y,x):
    # pr -> y,x -> x
    return x**4+6*y**0.5-10
def fy(x,y):
    # pr -> x,y -> y,
    return x**4+6*y**0.5-10

tol=1.0e-6
x,y=1,4
dfdx_y=dfdx3(fx,y,x,tol)
dfdy_x=dfdx3(fy,x,y,tol)
print(dfdx_y,dfdy_x,'exact=',4,3/2)