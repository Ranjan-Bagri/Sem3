# Trace of a matrix
def matTrace(A):
    trA=0
    for i in range(len(A)):
        trA+=A[i][i]
    return trA

# Scaler product of matrix
def matScp(s,A):
    return [[s*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Transpose of a matrix
def matTrans(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Matrix addition
def matSum(A,B):
    if len(A)!=len(B) or len(A[0]) != len(B[0]): # sizes doesn't match
        return None
    ApB=A.copy()
    for i in range(len(A)):
        for j in range(len(A[0])):
            ApB[i][j]=A[i][j]+B[i][j]
    return ApB

# Matrix multiplication
def matMul(A,B):
    col=len(A[0])
    row=len(B)
    if row != col:
        return None
    AB_row=len(A) # number of rows of AB matrix
    AB_col=len(B[0]) # number of columns of AB matrix
    AB=[[0.0 for i in range(AB_col)] for j in range(AB_row)] # AB initialized

    for i in range(AB_row):
        for j in range(AB_col):
            for k in range(row):
                AB[i][j]=AB[i][j]+A[i][k]*B[k][j]
    return AB