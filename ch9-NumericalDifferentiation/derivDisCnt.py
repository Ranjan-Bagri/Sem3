# Numerical derivative of discrete function transformed to continuous function
import sys
sys.path.append("../ch7-Interpolation/")
from disToCnt import *
from derivative import *
import numpy as np

def f(pr,x):
    # transformation to continuous function with Lagrange interpolation
    # pr[0]=x-array, pr[1]=f(x)-array,pr[2]=m
    fx=disToCnt(pr[0],pr[1],pr[2])
    return fx
def forDisFnc(x):
    # function to obtain the discrete function
    return np.sin(x)

# create discrete function
x,y=[],[]
xx=-2.2
while xx<=2.2:
    x.append(xx)
    y.append(forDisFnc(xx))
    xx+=0.1

m=5 # number of local interpolating points
pr=[x,y,m] # send the discrete function and m as parmeter
xx=-1.23 # x-value where derivative is to be determined
print(dfdx3(f,pr,xx,1.0e-8),np.cos(xx)) 