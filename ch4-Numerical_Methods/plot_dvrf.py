import numpy as np 
import matplotlib.pyplot as plt 
from derivative import deriv

def f(pr,x):
    return np.sin(x)

x,fx,df=[],[],[]
pr=None # parameter set to None
xx=-np.pi
while xx<np.pi:
    x.append(xx)
    fx.append(f(pr,xx))
    df.append(deriv(f,pr,xx,0.01))
    xx+=0.01

plt.plot(x,fx,'k-',label='f(x)')
plt.plot(x,df,'k:',label=r'$\frac{df}{dx}$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()