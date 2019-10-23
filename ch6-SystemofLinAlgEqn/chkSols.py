def chkSols(a,x,tol):
    # This is a utility python function. It verifies that
    # the values in the array x are really the solutions of the 
    # set of equations given by the augmented matrix a
    #
    # argumets 
    # a ==> augmented matrix corresponding to the given set of equations
    # x ==> array of values to be tested
    # tol ==> tolerence of verification
    # 
    # returns
    # chk ==> True, if verified successfully else False
    #
    n=len(x)
    q=0
    for i in range(n):
        sum=0
        for j in range(n):
            sum+=a[i][j]*x[j]
        sum-=a[i][n]
        if  abs(sum)<=tol:
            q+=1
    if q==n:
        chk=True
    else:
        chk=False
    
    return False