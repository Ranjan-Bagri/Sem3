# 1st order differentiation of the user defined continuous function
#
# arguments
# f,pr ==> user defined function with its parameter
# x ==> x-coordinate at which derivative is to be determined
# tol ==> tolerence of calculation
# returns
# dfdx2 ==> derivative at 'x'
#
def dfdx1(f,pr,x,tol):
    # derivative calculated with one point forward difference method
    h=0.1
    dfdx10=(f(pr,x+h)-f(pr,x))/h
    while True:
        h=h*0.5
        dfdx2=(f(pr,x+h)-f(pr,x))/h
        if abs(dfdx2-dfdx10)<=tol: # required tolerence is achieved
            break
        else:  # required tolerence is not achieved
            dfdx10=dfdx2
    return dfdx2

def dfdx3(f,pr,x,tol):
    # derivative calculated thre  point central difference method
    h=0.1
    dfdx1=(f(pr,x+h)-f(pr,x-h))/(2*h)
    while True:
        h=h*0.5
        dfdx2=(f(pr,x+h)-f(pr,x-h))/(2*h)
        if abs(dfdx2-dfdx1)<=tol: # required tolerence is achieved
            break
        else: # required tolerence is not achieved
            dfdx1=dfdx2
    return dfdx2

def dfdx5(f,pr,x,tol):
    # derivative calculated with five point central difference method
    h=0.1
    dfdx1=(f(pr,x-2*h)-8.0*f(pr,x-h)+8.0*f(pr,x+h)-f(pr,x+2*h))/(12*h)
    while True:
        h=h*0.5
        dfdx2=(f(pr,x-2*h)-8.0*f(pr,x-h)+8.0*f(pr,x+h)-f(pr,x+2*h))/(12*h)
        if abs(dfdx2-dfdx1)<=tol: # required tolerence is achieved
            break
        else: # required tolerence is not achieved
            dfdx1=dfdx2
    return dfdx2
