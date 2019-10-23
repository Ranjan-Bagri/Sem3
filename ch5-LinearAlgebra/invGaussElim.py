# Inverse by Gauss-Jordon eliminatin method

def invGaussElim(A):
    n=len(A)
    a=A.copy() # make a copy
    b=[[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)] #identity

    for i in range(n):
        for j in range(n):
            if j!=i:
                r=a[j][i]/a[i][i]
                for k in range(n):
                    a[j][k]=a[j][k]-r*a[i][k] # n^2-n numbers of row operations
                    b[j][k]=b[j][k]-r*b[i][k]

    for i in range(n):
        for j in range(n):
            b[i][j]=b[i][j]/a[i][i] # last n numbers of operations

    return b