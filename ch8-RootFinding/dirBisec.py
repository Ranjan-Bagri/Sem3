from math import *
def f(x):
    # user defined function
    return x**2-2*x-3

a,b=-3,0 # [a,b]
tol=1.0e-5 # tolerence
if f(a)*f(b)>0:
    print("f(a)f(b) < 0 is not satisfied in [a,b]")
else:
    while abs(b-a)>tol:
        x=(a+b)/2.0
        if f(a)*f(x)<0:
            b=x
        elif f(a)*f(x)>0:
            a=x
        else:
            if f(a)==0.0:
                x=a
            break
    print("Root is ",x)
    print('Verification')
    print("f(%.4f)=%.4f"%(x,f(x)))
