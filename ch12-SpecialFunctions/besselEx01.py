# Verification of J-n(x)=(-1)^n Jn(x)
from bessel import *
import numpy as np 
import matplotlibn=3
x,xx,Jnx,J_nx=-20.0,[],[],[]
while x<20.0:
    xx.append(x)
    JJ_n=recJn(-n,x)
    JJn=(-1)**n*recJn(n,x)
    Jnx.append(JJn)
    J_nx.append(JJ_n)
    x+=0.01

plt.plot(xx,J_nx,'k-',label=r'$J_{-n}{x}$')
plt.plot(xx,Jnx,'k.',markevery=15,label=r'$(-1)^n J_n(x)$')
plt.xlabel('x')
plt.legend()
plt.show()