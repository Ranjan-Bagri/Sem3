from bisec import bisec
from bracSol import bracSol

def f(pr,x):
    # User defined function f(x)=|x|-x^2-x+3
    # parameter pr=None from main
    if x>=0:
        fx=x-x**2-x+3
    else:
        fx=x-x**2-x+3
    return fx

# upper and lower bounds of solutions [a,b]
# range of non-existance of two consecutive roots is dx
a,b,dx=-4,2,1.2 # dx taken with guess
brack=bracSol(f,None,a,b,dx) # get the bracket of roots

if brack!=None: # if at least one bracket exists
    for i in brack: # iterate over the brackets
        x=bisec(f,None,brack,brack+dx,1.0e-8) # use bisection
        print("f(%f)=%f"%(x,f(None,x))) # print with verification
