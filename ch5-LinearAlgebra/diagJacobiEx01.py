from diagJacobi import diagJacobi
from matOpr import matMul, matScp

A=[[7,3,2,1],[3,9,-2,4],[2,-2,-4,2],[1,4,3,2]]
n=len(A)
a,x=diagJacobi(A,1e-5) # diagonalized matrix and eigen values

# check the eigen values and eigen vectors
# A.X=lmb.X

for j in range(n):
    xx=[[x[j][i]] for i in range(n)] # convert eigenvector to column matrix
    AX=matMul(A,xx) # matrix product A.X
    lmbX=matScp(a[j][j],xx) # matrix product lmb.X
    print('lmb        X       A.X ',' lmb.X')
    print('------------------------------')
    print('%.4f  %.4f  %.4f  %.4f'%(a[j][j],x[j][0],AX[0][0],lmbX[0][0]))
    for i in range(1,len(x)):
        print('%.4f  %.4f  %.4f'%(x[j][i],AX[i][0],lmbX[i][0]))
