# Determinant of a matrix by Gauss elimination with partial pivoting method

def det(A):
    n=len(A)
    a=A.copy() # make a copy
    #a=[[A[i][j] for j in range(n)] for i in range(n)]
    for i in range(n-1):
        # Partial pivoting
        mxa=a[i][i]
        m=i
        for j in range(i+1,n):
            if abs(a[j][i])>mxa:
                mxa=abs(a[j][i])
                m=j
        ta=a[i]
        a[i]=a[m]
        a[m]=ta

        for j in range(i+1,n):
            rat=a[j][i]/a[i][i]
            for k in range(n):
                a[j][k]=a[j][k]-rat*a[i][k] # all row operations

    det=1.0
    for i in range(n):
        det=det*a[i][i]
    
    return det