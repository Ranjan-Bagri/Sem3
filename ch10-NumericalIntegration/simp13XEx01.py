from math import * 
from simp13X import simp13X
def f(pr,x):
    return sin(x)
tol=1.0-6 # accuracy
a,b=pi/3,2*pi # limits
print(simp13X(f,None,a,b,tol)) # parameter set to None