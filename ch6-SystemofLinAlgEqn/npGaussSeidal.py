# Gauss-Seidal method using 'linalg' module in numpy
import numpy as np 
a=np.array([[9,1,1,1],[1,8,1,1],[1,1,7,1],[1,1,1,6]])
b=np.array([75,54,43,34])
xk_1=np.array([0,0,0,0]) # initial guess of solutions
tol=1.0e-5

L=np.tril(a)  # lower triangular matrix along with diagonal
U=a-L # Upper triangular matrix
n=len(xk_1)
while True:
    L_1=np.linalg.inv(L) # L^-1
    Ux=np.dot(U,xk_1) # U*x
    xk=np.dot(L_1,b-Ux) # xk=L^-1*(b-U*x)
    # convergence check
    iq=0
    for i in range(n):
        if abs(xk[i]-xk_1[i])<=tol:
            iq+=1
    if iq==n:
        break
    else:
        xk_1=[xk[i] for i in range(n)] # Xk_1 <-- xk
print('Solutions:',xk)
