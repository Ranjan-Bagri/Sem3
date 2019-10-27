import numpy as np 
from simp13Xdis import simp13Xdis

def f(x):
    # continuous function to obtain discrete function
    return np.exp(x)
h=1.0e-3
x,fx=[],[]
xx=0.0
while xx<=2.5:
    x.append(xx)
    fx.append(f(xx))
    xx+=h
print("Integration of the discrete function=",simp13Xdis(h,fx))