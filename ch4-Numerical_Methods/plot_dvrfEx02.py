import numpy as np 
import matplotlib.pyplot as plt 
from derivative import deriv

def f(n,x):
    return np.sin(x)**n
n=[2,3]
for i in n:
    x,fx,df=[],[],[]
    xx=-np.pi
    while xx<np.pi:
        x.append(xx)
        fx.append(f(i,xx))
        df.append(deriv(f,i,xx,0.01))
        xx+=0.01
        st="for n=%d"%i 
    
    plt.plot(x,fx,'k-',label='f(x)'+st)
    plt.plot(x,df,'k:',label=r'$\frac{df}{dx}$'+st)
    plt.legend(loc='best',prop={'size':12})
    plt.xlabel('x')
    plt.title(r"Plot of f(x) and $\frac{df}{dx}$,$f(x)=sin^n(x)$")
    plt.show()
    plt.clf()