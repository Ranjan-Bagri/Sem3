from bisec import bisec
def f(pr,x):
    # user defined function with parameter pr=None from main
    return x**3+2*x**2+2.2*x+0.4 # function f(x)

a=float(input("Enter the lower bound a:")) # upper bound as user input
b=float(input("Enter the lower bound b:")) # lower bound as user input
x=bisec(f,None,a,b,1.0e-6) # parameter =None, tol=1.0e-6
if x!=None: # if solution exists
    print("Solution is x=%f verification "%x)
    print("f(%f)=%.4f"%(x,f(None,x)))