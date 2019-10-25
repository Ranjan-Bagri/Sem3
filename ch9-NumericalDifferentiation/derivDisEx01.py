# Example of discrete forward difference
from derivDis import dfdx3Dis
import numpy as np 

def f(x): # analytic function
    return np.sin(x)
x,y=[],[]
xx=0.0
while xx<=3.0:
    x.append(xx)
    y.append(f(xx))
    xx+=0.01
i=200 # index of the x-value
print(x[i],np.cos(x[i],dfdx3Dis(x,y,x[i])))
# x-value exact derivative numerical derivative