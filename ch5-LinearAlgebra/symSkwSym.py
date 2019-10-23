from matOpr import *

a=[[1,2,3],[-2,3,-1],[-3,-2,1]]
at=matTrans(a)
mat=matScp(-1,at)

print(matScp(0.5,matSum(a,at)))
print(matScp(0.5,matSum(a,mat)))