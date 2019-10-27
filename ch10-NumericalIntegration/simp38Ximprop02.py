from simp38X import simp38X
import numpy as np 
def f(n,x):
    return np.exp(-x**2)

m=10
tol=1.0e-5
I0=0
while True:
    I=simp38X(f,None,-m,m,0.1*tol)
    if abs(I-I0)<tol:
        break
    I0=I
    m+=10
print('Value of the integral=',I)