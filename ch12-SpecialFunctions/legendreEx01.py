from legendre import *
import matplotlib.pyplot as plt  

n=4
xmn,xmx,dx=-1.0,1.0,0.01 # x-range and increment of x-values
for i in range(n):
    x,xx=xmn,[]
    LgnDir,Lgn=[],[]
    while x<xmx:
        xx.append(x)
        LgnDir.append(Pn(i,x))
        Lgn.append(recPn(i,x))
        x+=dx
    plt.plot(xx,Lgn,'k',label=r'Recursive $P_%d(x)$'%i)
    plt.plot(xx,LgnDir,'k.',markevery=6,label=r'Direct $P_%d(x)$'%i)
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()