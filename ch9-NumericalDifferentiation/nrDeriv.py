from derivative import dfdx3

def nrDeriv(f,pr,x1,mx_itr,tol):
    # Newton-raphson method for solving with numerical derivative
    # 
    # arguments
    # f,pr ==> user defined function with its parameters
    # x1 ==> initial guess x-coordinates
    # mx_itr ==> maximum number of iterations allowed
    # tol ==> tolerence of calculation
    # returns
    # x2 ==> the solution
    itr=0
    while True:
        x2=x1-f(pr,x1)/dfdx3(f,pr,x1,tol)
        if abs(x2-x1)<=tol or itr>mx_itr:
            break
        else:
            x1=x2
        itr+=1
    if itr<mx_itr:
        return x2
    else:
        return None
