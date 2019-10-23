from GaussSeidalMat import GaussSeidalMat
a=[[10,-2,-1,-4,3],[-2,10,-1,-1,15],[-1,-1,10,-2,27],[-1,-1,-2,10,-9]]
x=GaussSeidalMat(a)
print("Solutions:%.3f"%x[0],end='')
for i in range(1,len(x)-1):
    print("%.3f"%x[i],end='')
print("%.3f"%x[len(x)-1])