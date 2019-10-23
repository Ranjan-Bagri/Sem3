# Gauss Seidal Method for solving linear simultaneous equations
def GaussSeidal(a,tol):
    # arguments
    # a ==> array a[i][j], for each i=0,1,...,n-1,j=0,1,..,n
    # tol ==> tolerence of roots
    # 
    # returns
    # x1 ==> array of solutions, x1[i] for i=0,1,..,n-1
    #
    # N.B:  number of iterations (it) has been calculated but not returned.
    # If required then it can be returned
    n=len(a) # number of rows, number of columns =n+1
    iq=0 # count to check all the rows are diagonally dominant
    # check for diagonally dominant
    for i in range(n):
        sum=0.0
        for j in range(n):
            if j!=i:
                sum+=abs(a[i][j])
        if abs(a[i][i]>=sum):
            iq+=1
    if iq != n: # Diagonally dominant not satisfied
        print("Matrix is not diagonally dominant. Quitting")
        return None
    
    # Diagonally dominant satisfied
    # Two arrays to store values of the variables for two consecutive iterations
    x0=[0.0 for i in range(n)] # initialized to zero
    x1=[0.0 for i in range(n)]
    it=1 # counter for iterations
    
    while True:
        iq=0 # counter to check convergence of all variables
        for i in range(n):
            x1[i]=a[i][n] # nth column of augmented matrix
            for j in range(n):
                if j!=i:
                    x1[i]=x1[i]-a[i][j]*x1[j]
            x1[i]=x1[i]/a[i][i]
            if abs(x1[i]-x0[i])<=tol:
                iq+=1
        if iq==n: # all variables converged,means solutions obtained
            break
        else:
            # some of the variables not converged, so iteration continues with new assignments of values
            x0=[x1[i] for i in range(n)]
            it+=1

    return x1