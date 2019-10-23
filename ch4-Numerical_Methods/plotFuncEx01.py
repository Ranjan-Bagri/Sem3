import numpy as np 
import matplotlib.pyplot as plt 

from FuncEx01 import f 

lnsty=['k-','k--','k--.','k:']
x=np.arange(0.0,3.0,0.01)
a=[-0.25,-0.5,-0.70,-0.85]
b=[3.5,3.7,4.2,4.5]

for i in range(len(a)):
    pr=[a[i],b[i]]
    fx=f(pr,x)
    st="a=%.2f,b=%.2f"%(a[i],b[i])
    plt.plot(x,fx,lnsty[i],label=st)

plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.title(r'Plot of $e^{ax}sin{bx}$')
plt.show()