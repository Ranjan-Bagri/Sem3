import numpy as np 
from trpzX import trpzX
def f(pr,x):
    return x**0.5*np.exp(x)
a,b=0,np.pi
tol=1.0e-6
I=trpzX(f,None,a,b,tol) # parameter set to none
print('value of the integral=',I)