# Demonstration of tangent and Normal
import matplotlib.pyplot as plt 
from derivative import dfdx3

def f(pr,x):
    # user defined function with parameter set None from main
    return x**2
tol=1.0e-6
x0=0.5
m=dfdx3(f,None,x0,tol) # slope of f(x) at x=x0
mp=-1.0/m # slope of normal at x=x0

# collection of data for plotting
x,y,tng,nor=[],[],[],[]
xx=-2.0 # initial x-value
while xx <= 2.0: # final x-value
    x.append(xx)
    y.append(f(None,xx)) # data for f(x)
    tng.append(f(None,x0)+m*(xx-x0)) # data for tangent
    nor.append(f(None,x0)+mp*(xx-x0)) # data for normal
    xx+=0.1 # increment of x-value

# visualization
plt.axes().set_aspect('equal') # for equal aspect ratio
plt.plot(x,y,label='f(x)')
plt.plot(x,tng,label='tangent')
plt.plot(x,nor,label='normal')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.title('Demonstration of tangent and normal of a function')
plt.show()