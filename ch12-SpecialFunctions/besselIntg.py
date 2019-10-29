from math import *
import sys
sys.path.append('../ch10-NumericalIntegration/')
from simp13X import simp13X

def intJn(n,x):
    # integral representation of bessel function
    # arguments:
    # n ==> integer order of bessel function
    # x ==> at which bessel function is to be determined
    # returns: value of the bessel function
    def f(pr,th):
        # integral for bessel function
        return cos(pr[0]*th-pr[1]*sin(th))
    pr=[n,x]
    return (1/pi)*simp13X(f,pr,0.0,pi,1.0e-6)