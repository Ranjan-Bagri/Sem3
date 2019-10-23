# Gussian elimination method with partial pivoting for solving linear algebraic system of equations

def GaussElim(A):
    # Arguments:
    # A ==> 2d [n x n+1] augmented matrix corresponding to the system of equations
    # Returns
    # X ==> the array of solutions [x_0,x_1,...,x_{n-1}]
    #
    n=len(A)
    a=A.copy() # make a copy

    # Elimination process
    for i in range(n-1):
        # Partial pivoting
        mxa=a[i][i]
        m=i
        for j in range(i+1,n):
            if abs(a[j][i])>mxa:
                mxa=abs(a[j][i])
                m=j
        ta=a[i] # row exchange
        a[i]=a[m]
        a[m]=ta

        for j in range(i+1,n):
            cf=a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k]=a[j][k]-cf*a[i][k]
    
    # Back substitution process
    X=[0.0 for i in range(n)]
    X[n-1]=a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        sum=0.0
        for j in range(i+1,n):
            sum+=a[i][j]*X[j]
        X[i]=1.0/a[i][i]*(a[i][n]-sum)
    return X