from simp13XarcLen import simp13XarcLen
import numpy as np 
def f(pr,x):
    return np.sin(x)
tol=1.0e-5
arln=simp13XarcLen(f,None,0,2*np.pi,tol)
print('Arc length=',arln)