# Gauss-Seidal matrix method for solving linear algebraic system of equations
#
def GaussSeidalMat(a,tol=1.0e-5):
    # arguments:
    # a ==> 2d [n x n+1] augmented matrix corresponding to the system of equations
    # tol ==> tolerence for convergence of each solution default =1e-5
    #
    # returns:
    # xk ==> the array of solutions [[x_0],[x_1],...,[x_{n-1}]]

    import sys
    sys.path.append('../ch5-LinearAlgebra/')
    from matOpr import matMul,matSum,matScp
    from invGaussElim import invGaussElim

    n=len(a)
    L=[[0 for j in range(n)] for i in range(n)]
    U=[[0 for j in range(n)] for i in range(n)]
    b=[[0] for i in range(n)]

    for i in range(n):
        for j in range(n+1):
            if j<=i:
                L[i][j]=a[i][j] #L
            elif j>i and j<=n-1:
                U[i][j]=a[i][j] #U
            else:
                b[i][0]=a[i][j] #b
    
    xk_1=[[0] for i in range(n)] # x^(k-1)
    while True:
        Ux=matMul(U,xk_1) #Ux
        mUx=matScp(-1,Ux) # -Ux
        bpmUx=matSum(b,mUx) # b-Ux
        invL=invGaussElim(L) # L^-1
        xk=matMul(invL,bpmUx) # x^k = L^-1(b-Ux)
        iq=0
        for i in range(n):
            if abs(xk[i][0]-xk_1[i][0])<=tol: # |x^k - x^(k-1)|<=tol
                iq+=1
        if iq==n: # all solutions converged
            break
        else: # not converged
            xk_1=[[xk[i][0]] for i in range(n)] # x^(k-1)<--x^k
    
    x=[xk[i][0] for i in range(n)] # column matrix to vector
    return x