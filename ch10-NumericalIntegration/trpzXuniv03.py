import numpy as np 
from trpzX import trpzX
def f(pr,x):
    return np.cos(x)/x**4
tol=1.0e-6
a,b=np.pi/3,np.pi/2
I=trpzX(f,None,a,b,tol)
print('Value of the integration=',I)