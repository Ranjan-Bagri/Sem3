# Gamma function, Gamma(>=0.5)
from simp38X import simp38X
import numpy as np 
def f(n,x):
    return x**(2*n-1)*np.exp(-x**2) # gamma function

n=float(input('n='))
m=10
tol=1.0e-4 # tolerence reduced for faster convergence
I0=0
while True:
    I=simp38X(f,None,1,m,0.1*tol)
    if abs(I-I0)<tol:
        break
    I0=I
    m+=10
print("Gamma(%.2f)=%.4f"%(n,2*I))