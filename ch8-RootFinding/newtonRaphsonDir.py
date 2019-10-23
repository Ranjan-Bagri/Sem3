from math import sin,cos
def f(x):
    return x**2-sin(x)
def dfdx(x):
    return 2*x-cos(x)

tol=1.0e-6 # tolerence of calculation
mx_itr=1000 # maximum number of allowed iterations
x1=float(input("Put the initial guess:"))
itr=0
while True:
    x2=x1-f(x1)/dfdx(x1) # iteration to next point
    if abs(x2-x1)<=tol or itr > mx_itr: # exit point
        break
    else:
        x1=x2
        itr+=1 # next iteration
    
if itr < mx_itr:
    print("Solution is x = %9.5f"%x2)
    print("Verification f(%9.5f)=%9.5f"%(x2,f(x2)))
else:
    print("No solution found, Maximum iteration reached")