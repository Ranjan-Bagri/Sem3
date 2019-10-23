from matOpr import matMul, matSum, matScp
a=[[1,2,3],[-2,3,-1],[-3,-2,1]]
n=5 # order of polynomial
an=1 # co-efficient of polynomial
b=sa=[[1,0,0],[0,1,0],[0,0,1]]

for i in range(n):
    an=an*(1/(i+1)) # get co-efficent of an
    c=matMul(a,b) # c=ab
    b=c.copy() # b=c
    c=matScp(an,c) # c=an x c
    sa=matSum(sa,c) # sa=sa+c

print('Sum of the polynomial series=',sa)