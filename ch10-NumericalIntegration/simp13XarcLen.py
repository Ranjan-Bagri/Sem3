# Find the arc length
import sys
sys.path.append('../ch9-NumericalDifferentiation/')
from derivative import dfdx1 
from simp13X import simp13X

def dArcLen(nwPr,x):
    f,pr=nwPr[0],nwPr[1] # nwPr decomposed as function and its parameter
    fp=dfdx1(f,pr,x,1.0e-5) # get the derivative
    return (1+fp**2)**0.5 # return function which will be integrated
def simp13XarcLen(f,pr,a,b,tol): # function to determine arc length
    # arguments:
    # f ==> user defined function of which arc length is to be determined
    # pr ==> parameter corresponding to the function
    # a ==> initial point of arc
    # b ==> final point of arc
    # tol ==> tolerence
    # returns:
    # arcLen ==> arc length on the curve f(pr,x) from x=a to x=b

    nwPr=[f,pr] # parameter array contains user function and its parameter
    arclen=simp13X(dArcLen,nwPr,a,b,tol) # integral for arc length
    return arclen