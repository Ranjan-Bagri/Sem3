from simp13XarcLen import simp13XarcLen
def f(a,x): # locus of circle of kradius a
    return (a**2-x**2)**0.5
tol=1.0e-5
a=1.0
arln=simp13XarcLen(f,a,-a,a,tol) # parameter=a
print('Arc length=',arln)