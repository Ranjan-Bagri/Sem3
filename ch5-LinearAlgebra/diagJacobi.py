# Diagonalization of a symmetric matrix by Jacobi Method
def diagJacobi(A,tol):
    # A ==> Input symmetric matrix to be diagonalized
    # tol ==> Tolerence for convergence of each off-diagonal matrix
    # returns
    # a ==> Diagonalied matrix
    # x ==> eigen vector matrix, each row is an eigen vector
    from math import pi, cos, sin, atan
    from matOpr import matMul, matTrans
    n=len(A)
    a=A.copy()
    cnvg=False
    x=[[1 if i==j else 0 for j in range(n)] for i in range(n)] # eigen vectors
    # check if already the matrix is diagonalized
    iq=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                if abs(a[i][j])>tol:
                    iq+=1
    
    if iq==0:
        cnvg=True
        a,x=None

    it=0 # iteration count
    while not cnvg:
        it+=1
        # Get the highest off-diagonal matrix
        i,j,amx=0,1,a[0][1] # initial values
        for p in range(n):
            for q in range(n):
                if p!=q:
                    if abs(a[p][q])>amx:
                        i,j,amx=p,q,abs(a[p][q])
        # position of highest off-diagonal term is (i,j)
        # Determine theta for given transformation P(i,j,theta)
        if a[i][i]==a[j][j]:
            if a[i][j]>0:
                th=pi/4
            else:
                th=-pi/4
        else:
            th=0.5*atan(2*a[i][j]/(a[i][i]-a[j][j])) # theta
        cs,sn=cos(th),sin(th)

        # Constuction of P matrix
        P=[[1 if p==q else 0 for q in range(n)] for p in range(n)]
        P[i][i]=P[j][j]=cs
        P[j][i],P[i][j]=sn,-sn

        # Construction of PT matrix
        PT=[[1 if p==q else 0 for q in range(n)] for p in range(n)]
        PT[i][i]=PT[j][j]=cs
        PT[j][i],PT[i][j]=-sn,sn

        # The Given's transformation : a <-- P^TaP
        PTA=matMul(PT,a) #  P^Ta
        a=matMul(PTA,P) # P^TaP
        x=matMul(x,P) # Column wise eigen vectors matrix

        ## check convergence, each off-diagonal term <= tol
        iq=0
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if abs(a[i][j])>tol:
                        iq+=1
        if iq==0:
            cnvg=True
        x=matTrans(x) # convert column wise to row wise eigen vectors matrix
        return a,x