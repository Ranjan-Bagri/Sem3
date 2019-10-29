# Verification of Jn-1(x)-Jn+1(x)=2J'(x)
import matplotlib.pyplot as plt 
from bessel import Jn
import sys
sys.path.append('../ch9-NumericalDifferentiation/')
from derivative import dfdx3

n=0
x=-10.0
xx,yy1,yy2=[],[],[]
while x<=10.0:
    xx.append(x)
    yy1.append(Jn(n-1,x)-Jn(n+1,x))
    yy2.append(2*dfdx3(Jn,n,x,1.0e-6))
    x+=0.1
plt.plot(xx,yy1,'k-',label=r'$J_{n-1}(x)-J_{n+1}(x)$')
plt.plot(xx,yy2,'k.',markevery=3,label=r'$2J_n^\prime(x)$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()