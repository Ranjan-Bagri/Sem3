# work done \int f(x) dx
import numpy as np 
from simp13X import simp13X
def f(pr,x): # force
    return np.cos(np.pi*x)
tol=1.0-6 # accuracy
a,b=0,0.5 # limits
print('Work done=',simp13X(f,None,a,b,tol),'units') # parameter set to None