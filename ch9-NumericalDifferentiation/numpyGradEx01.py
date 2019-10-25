import numpy as np 
f=np.array([1,2,4,7,11,16]) # discrete function
# uniform
print(np.gradient(f)) # uniform step length with value 1.0
print(np.gradient(f,2)) # uniform step length with value 2.0

# non-uniform
x=np.array([0.0,1.0,1.5,3.5,4.0,6.0]) # array of step lengths, array lengths of f and x must be same
print(np.gradient(f,x))