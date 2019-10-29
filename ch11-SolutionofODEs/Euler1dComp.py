# Comparison of step length in Euler method
import matplotlib.pyplot as plt 
import numpy as np 
from Euler1d import Euler1d

def f(pr,x,y):
    return 4.0*x 

# below array of line styles for plotting
lct=['k--','k-.','k:']
x,y=0.0,0.0 # initial values of x and y
h,X=0.01,10.0 # values of initial step length and final values of x
xx=np.arange(0.0,10.0,0.5) # numpy array for plotting exact result for comparison
i=0
while h<1.05: # loop over step length
    x,y=0.0,0.0
    x,y,dydx=Euler1d(f,None,x,y,h,X)
    tt="h=%.4f"%h # concatenation of string for plot title
    plt.plot(x,y,lct[i],label=tt)
    h+=0.5
    i+=1
plt.plot(xx,2*xx**2,'k',label='Exact Solution')
plt.legend(loc='best',prop={'size':12})
plt.title("Comparison among different step length for euler method")
plt.xlabel('x')
plt.ylabel('y')
plt.show()