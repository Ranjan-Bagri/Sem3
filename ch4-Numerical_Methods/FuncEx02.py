from derivative import deriv
def f(pr,x):
    return x**2
print(deriv(f,None,3.97,0.01)) # pr=None,x=3.947,h=0.01