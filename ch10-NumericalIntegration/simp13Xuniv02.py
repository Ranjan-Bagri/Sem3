import numpy as np 
from simp13X import simp13X
def f(pr,x):
    return np.exp(-(x-1)**2)
tol=1.0-6 # accuracy
a,b=-2,4 # limits
print(simp13X(f,None,a,b,tol)) # parameter set to None