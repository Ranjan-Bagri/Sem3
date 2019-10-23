from math import *
from bisec import bisec

def f(fx,x):
    # User defined function with parameter fx (string)
    return eval(fx)

fx=input("Enter the function of x :") # user inserted function
a=float(input("Enter the lower bound a :")) # upper bound of [a,b]
b=float(input("Enter the upper bound b :")) # lower bound of [a,b]

x=bisec(f,fx,a,b,1.0e-5) # parameter fx, tolerence=10^-5
if x!=None:
    print("f(%.3f)=%.5f"%(x,f(fx,x)))