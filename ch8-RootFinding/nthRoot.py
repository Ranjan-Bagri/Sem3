from bisec import bisec
def f(pr,x):
    # parameter pr =[n.alp] # alp == > alpha
    return x**pr[0]-pr[1]

n,alp=3,2.0
pr=[n,alp]
a,b=0,alp
x=bisec(f,pr,a,b,1.0e-6) # get the root
print('Root is ',x)
print('Verification of root,f(%.5f)=%.5f'%(x,f(pr,x)))
