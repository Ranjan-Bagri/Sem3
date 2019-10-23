from bisec import bisec
from bracSol import bracSol
from math import sin

def f(pr,x):
    return x**2*sin(x)

a,b,dx=-10,10,1.2 # dx taken with a guess
brack=bracSol(f,None,a,b,dx) # get brackets of roots

if brack!=None:
    for i in brack:
        x=bisec(f,None,brack,brack+dx,1.0e-8) # use bisection to get roots
        print("f(%f)=%f"%(x,f(None,x))) # print with verification
