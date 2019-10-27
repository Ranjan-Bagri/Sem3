from math import * 
from simp38X import simp38X
def f(pr,x):
    return sin(x)
tol=1.0e-5
a,b=pi/3,2*pi
print('Integral=',simp38X(f,None,a,b,tol))