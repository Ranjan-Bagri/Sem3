from nrDeriv import nrDeriv

def f(pr,x):
    return x**2-3*x+2
mx_itr=1000
x1=float(input("Enter the initial guess: "))
x=nrDeriv(f,None,x1,mx_itr,1.0e-6)
if x!=None:
    print("Solution is x=%9.5f"%x)
    print("Verification f(%9.5f)=%9.5f"%(x,f(None,x)))
else:
    print("No solution found, Maximum iteration reached")