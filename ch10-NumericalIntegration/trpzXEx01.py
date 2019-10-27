from math import *
from trpzX import trpzX 
def f(pr,x):
    # user defined function with parameter set to None
    return sin(x)

tol=1.0e-6
a,b=pi/3,2*pi
I=trpzX(f,None,a,b,tol) # calculated value of the integration
ext=cos(pi/3)-cos(2*pi)
print('calculated=',I,', exact=',ext)