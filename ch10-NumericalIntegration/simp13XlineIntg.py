# Perform line integral over a curve can be represented in parametric form
import sys
sys.path.append('../ch9-NumericalDifferentiation/')
from derivative import dfdx3
from simp13X import simp13X

def dAdr(fnPr,t):
    # parameter ==> fnPr=[[Ax,Ay,..],[x,y,...],[pr0,pr1,...],tol]
    # variable ==> t
    n=len(fnPr)
    ln=len(fnPr[1])
    ft=0
    for i in range(ln):
        # ft =Ax([pr0,pr1,..],t)*dfdx3(x(t),pr0,t,tol)+...
        ft+=fnPr[0][i](fnPr[2],t)*dfdx3(fnPr[1][i],fnPr[2][i],t,fnPr[n-1])
    return ft

def simp13XlineIntg(fnPr,t0,t1,tol):
    # arguments:
    # fnPr ==> array containing functions [[A_x,A_y,...],[x,y,..],[pr0,pr1,..],tol]
    # t0 ==> lower limit of integral
    # t1 ==> upper limit of integral
    # tol ==> tolerence of calculation of integral
    # returns:
    # lineIntg ==> the value of the line integral
    # 
    # N.B ==> tolerences of calculation of differentiations and integral are same
    fnPr.append(tol) # tolerence is appeneded in the parameter
    lineIntg=simp13X(dAdr,fnPr,t0,t1,tol)
    return lineIntg
