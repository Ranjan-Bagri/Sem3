from newtonRaphson import nr
def f(pr,x):
    return x**3+2*x**2+2.2*x+0.4

def dfdx(pr,x):
    return 3*x**2+4*x+2.2

tol=1.0e-6 # tolerence of calculation
mx_itr=1000 # maximum number of allowed iterations
x0=float(input("Put the initial guess:"))
# obtain the solution with user defined functions and parameters as None
x=nr(f,None,dfdx,None,x0,mx_itr,tol)
if x!= None: # solutions obtained within mx_itr number of iterations
    print("Solution is x = %9.5f"%x)
    print("Verification f(%9.5f)=%9.5f"%(x,f(None,x)))
else: # solution not obtained within mx_itr number of iteration
    print("No solution found, Maximum iteration reached")
