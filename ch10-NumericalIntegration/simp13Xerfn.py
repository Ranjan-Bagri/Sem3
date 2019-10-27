import numpy as np 
import matplotlib.pyplot as plt 
from simp13X import simp13X

def erfn(x): # error function
    def f(pr,t): # function in error function
        return np.exp(-t**2)
    tol=1.0e-5
    erf=simp13X(f,None,0,x,tol) # integration in error function
    return erf # return value of error function for x=x
xx,yy=[],[] # collect the values x and erf(x)
x,X,dx=0,5,0.01
while x<X:
    xx.append(x)
    yy.append(erfn(x))
    x+=dx
plt.plot(xx,yy,label='f(x)') # plot of error function
plt.legend(loc='best',prop={'size':12}) # label of the plot
plt.xlabel('x') # x-axis title
plt.show()