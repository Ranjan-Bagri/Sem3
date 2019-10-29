# Orthogonality relation
import sys
sys.path.append('../ch10-NumericalIntegration/')
from simp13X import simp13X
from legendre import recPn

def PmPn(pr,x):
    return recPn(pr[0],x)*recPn(pr[1],x)
tol=1.0e-8
n=6
I=simp13X(recPn,n,-1,1,tol)
m=4
for i in range(3,n+1):
    I=simp13X(PmPn,[m,i],-1,1,tol) # parameter [m,i]
    print("(2 x %d+1)/2 P%d P%d=%f"%(i,m,i,I*(2*i+1)/1))
