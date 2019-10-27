import numpy as np 
from trpzX import trpzX 

def f(pr,x):
    return x**2.5*np.exp(-x)
tol=1.0-6
a,b=np.pi/2,np.pi
I=trpzX(f,None,a,b,tol) # parameter set to None
print('Value of the integration=',I)