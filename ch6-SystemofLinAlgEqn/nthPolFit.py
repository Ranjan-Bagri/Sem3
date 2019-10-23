# Fit a polynomial with given set of data by Gauss Elimination Method

def nthPolFit(k,x,y):
    # arguments
    # k ==> degree of the polynomial to be fit
    # x ==> 1d array of x-coordinates of discrete function
    # y ==> 1d array of y-copordinates of the discrete function
    # 
    # returns
    # a ==> array of coefficients of the polynomial
    #
    from GaussElim import GaussElim
    n=len(x)
    XX=[0.0 for i in range(2*k+1)]
    for i in range(2*k+1):
        for j in range(n):
            XX[i]+=x[j]**i
    
    XY=[0.0 for i in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            XY[i]+=x[j]**i*y[j]
    
    X=[[0.0 for j in range(k+2)] for i in range(k+1)] # X matrix
    for i in range(k+1):
        for j in range(k+1):
            X[i][j]=XX[i+j]
        X[i][k+1]=XY[i]
    a=GaussElim(X)
    return a