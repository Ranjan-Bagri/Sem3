# cos(x)=J0(x)+2\sum_{n=1}^\infty(-1)^n J2n(x)
import numpy as np 
import matplotlib.pyplot as plt 
from bessel import Jn

x=-10.0
xx,yy1,yy2=[],[],[]
tol=1.0e-5 # convergence tolerence
while x<=10.0:
    xx.append(x)
    n=0
    sJ2n=Jn(n,x)
    while True:
        n+=1
        trm=(-1)**n*Jn(2*n,x) # term of each iteration
        sJ2n+=2*trm
        if abs(trm)<tol:
            break
    yy2.append(np.cos(x)) # cos(x)
    x+=0.1
    yy1.append(sJ2n) # right hand side

plt.plot(xx,yy1,'k',label=r'$J_0(x)+2\sum_{n=1}^\infty(-1)^n J_{2n}(x)$')
plt.plot(xx,yy2,'k.',label=r'$\cos(x)$')
plt.legend(loc='best',prop={'size':12})
plt.show()