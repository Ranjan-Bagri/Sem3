from scipy.misc import derivative
from math import * 
def f(x,a):
    return exp(a*x)

def fct(k):
    fc=1
    for i in range(1,k+1):
        fc*=i
    return fc
b=-1.50 # arbitrary value of 'a' in f()
d=5
x=1.567 # the test point
for n in range(1,6):
    m=2*n+1
    h=10**(-d/n)
    drv=derivative(f,0.0,h,n=n,args=(b,),order=m) # derivative at x=0
    tyTrm=drv*x**n/fct(n) # taylor series term
    exc=(b*x)**n/fct(n) # exact term
    print('%.5f %.5f'%(exc,tyTrm))