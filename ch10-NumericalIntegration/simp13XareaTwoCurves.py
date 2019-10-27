# To find the area between two curves

import sys
sys.path.append('../ch8-RootFinding/')
from bisec import bisec # bisection method to obtain solution
from simp13X import simp13X # integration to obtain area

def f0_f1(fp,x):
    # difference of two curves
    # arguments:
    # fp ==> array of two functions and parameters of those functions
    # fp=[f0,pr0,f1,pr1]
    # returns:
    # difference between two functions with parameters
    return fp[0](fp[1],x)-fp[2](fp[3],x)

def getIntsec(f0,pr0,f1,pr1,a,b,dx,tol):
    # function to obtain the intersecting points
    # arguments:
    # f0(pr0,x),f1(pr1,x) ==> two functions of those intersections to be determined
    # a,b ==> the range within which the intersections to be determined
    # dx ==> interval of no solution
    # tol ==> tolerenceof solution
    # returns:
    # xx ==> array of x values of intersection points
    fp=[f0,pr0,f1,pr1]
    x=a
    xx=[]
    while x<b:
        if f0_f1(fp,x)*f0_f1(fp,x+dx)<0: # get the bound of intersection
            xx.append(bisec(f0_f1,fp,x,x+dx,tol)) # get intersecting points
        x+=dx
    return xx

def getArea(f0,pr0,f1,pr1,a,b,dx,tol):
    # function to obtain the area between two curves
    # arguments:
    # f0(pr0,x),f1(pr1,x) ==> two functions of those intersections to be determined
    # a,b ==> the range within which the intersection to be determined
    # dx ==> range of no solution
    # tol ==> tolerence of solution
    # returns:
    # x ==> array of x values of intersection points
    # area ==> total area under those two above curves
    x=getIntsec(f0,pr0,f1,pr1,a,b,dx,tol) # all intersecting points
    area=0
    for i in range(len(x)-1):
        I1=simp13X(f0,pr0,x[i],x[i+1],tol)
        I2=simp13X(f1,pr1,x[i],x[i+1],tol)
        area+=abs(I2-I1) # area between two curves
    return x,area