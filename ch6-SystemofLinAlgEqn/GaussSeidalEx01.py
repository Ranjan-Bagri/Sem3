from GaussSeidal import GaussSeidal
from chkSols import chkSols

# augmented matrix
a=[[10,-2,-1,-4,3],[-2,10,-1,-1,15],[-1,-1,10,-2,27],[-1,-1,-2,10,-9]]
tol=1.0e-5
x=GaussSeidal(a,tol)
ifSols=chkSols(a,x,tol)

"""
if ifSols:
    print("Solutions :",end='')
    for i in range(len(x)-1):
        print("%.3f"%x[i],end=',')
    print("%.3f"%x[len(x)-1])
else:
    print("Solutions obtained not satisfying set of equations.")
"""

print("Solutions :",end='')
for i in range(len(x)-1):
    print("%.3f"%x[i],end=',')
print("%.3f"%x[len(x)-1])