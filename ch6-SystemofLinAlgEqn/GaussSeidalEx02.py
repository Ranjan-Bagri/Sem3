from GaussSeidal import GaussSeidal
from chkSols import chkSols

# get the augmented matrix
fr=open("GSmat.dat","r")
a=[]
while True:
    line=fr.readline()
    if not line:
        break
    aa=[]
    for i in line.split():
        aa.append(float(i))
    a.append(aa)
fr.close()

tol=1.0e-5
x=GaussSeidal(a,tol)
ifSols=chkSols(a,x,tol)

if ifSols:
    print("Solutions:",end='')
    for i in range(len(x)-1):
        print("%.3f"%x[i],end='')
    print("%.3f"%x[len(x)-1])
else:
    print("Solutions obtained not satisfying set of operations.")