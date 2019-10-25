from scipy.misc import derivative
 
import matplotlib.pyplot as plt 

def f(x,p1,p2):
    return x**p1+x**p2
xFirst=True # for recording of x-values once
d=4
x,dydxn=[],[]
p,q=3,4
for n in range(1,5):
    m=2*n+1
    h=10**(-d/n)
    xx=0
    yp=[]
    while xx<=3.0:
        if xFirst:
            x.append(xx)
        yp.append(derivative(f,xx,h,n=n,args=(p,q),order=m))
        xx+=0.05
    dydxn.append(yp)
    xFirst=False

for n in range(4):
    plt.plot(x,dydxn[n],label=r'$f^%d$(x)'%(n+1))
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()