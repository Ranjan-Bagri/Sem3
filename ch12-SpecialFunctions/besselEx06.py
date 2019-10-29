# Verification of Jn-1(x)-Jn+1(x)=2J'(x)
import matplotlib.pyplot as plt 
from bessel import Jn
from besselIntg import intJn

n=0
x=-10.0
xx,yy1,yy2=[],[],[]
while x<=10.0:
    pr=[n,x]
    xx.append(x)
    yy1.append(intJn(n,x))
    yy2.append(Jn(n,x))
    x+=0.1
plt.plot(xx,yy1,'k-',markevery=3,label=r'Integral $J_%d(x)$'%n)
plt.plot(xx,yy2,'k.',label=r'Direct $J_%d(x)$'%n)
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()