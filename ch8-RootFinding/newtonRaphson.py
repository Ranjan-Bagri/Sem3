def nr(f,pr1,dfdx,pr2,x1,mx_itr,tol):
    # Newton-Raphson method with user defined derivative function
    # 
    # arguments
    # f,pr1 ==> user defined function with its parameter
    # dfdx,pr2 ==> user defined derivative function with parameter
    # x1 ==> initial guess
    # mx_itr ==> maximum number of iteration
    # tol ==> tolerence of calculation
    # 
    # return
    # x2 ==> the solution
    #
    itr=0
    while True:
        x2=x1-f(pr1,x1)/dfdx(pr2,x1) # iteration to next point
        if abs(x2-x1)<=tol or itr > mx_itr: # exit point
            break
        else:
            x1=x2
            itr+=1 # next iteration
    
    if itr < mx_itr:
        return x2
    else:
        return None