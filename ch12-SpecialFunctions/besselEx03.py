#    d
#   --  [x^-n Jn(x)]=-x^n Jn+1(x)
#   dx
import matplotlib.pyplot as plt 
from bessel import Jn
import sys
sys.path.append('../ch9-NumericalDifferentiation/')
from derivative import dfdx3

def xJn(n,x):
    # parameter ==> n
    return x**(-n)*Jn(n,x)

n=1
x=-10.0
xx,yy1,yy2=[],[],[]
while x<=10.0:
    xx.append(x)
    yy1.append(x**(-n)*Jn(n+1,x))
    yy2.append(2*dfdx3(xJn,n,x,1.0e-6))
    x+=0.1
plt.plot(xx,yy1,'k-',label=r'$x^{-n} J_{n+1}(x)$')
plt.plot(xx,yy2,'k.',markevery=3,label=r'$\frac{d}{dx}(x^(-n) J_n(x))$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()