# Derivative of an analytical function
import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return np.sin(x)*x**2

h=0.1
x=np.arange(-20,2.0,h)
y=f(x) # y-values same length of x-values

dydx=np.gradient(y,h,edge_order=2) # derivative

plt.plot(x,y,'k',label='y(x)')
plt.plot(x,dydx,'k:',label=r'$y^\prime(x)$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()