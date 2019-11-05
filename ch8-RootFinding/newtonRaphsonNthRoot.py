from newtonRaphson import nr

def f(pr,x):
    # user defined function with parameter pr=[n,a]
    return x**pr[0]-pr[1]

def dfdx(pr,x):
    return pr*x**(pr-1)

tol=1.0e-6 # tolerence of calculation
mx_itr=1000 # maximum number of allowed iterations
x0=float(input("Put the initial guess:"))
n,a=3,8 # 8^(1/3)
# obtain the solution with user defined functions and parameters as None
pr1,pr2=[n,a],n
x=nr(f,pr1,dfdx,pr2,x0,mx_itr,tol)
if x!= None: # solutions obtained within mx_itr number of iterations
    print("Solution is x = %9.5f"%x)
    print("Verification f(%9.5f)=%9.5f"%(x,f(pr1,x)))
else: # solution not obtained within mx_itr number of iteration
    print("No solution found, Maximum iteration reached")
