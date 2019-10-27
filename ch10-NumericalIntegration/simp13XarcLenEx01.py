from simp13XarcLen import simp13XarcLen
def f(m,x):
    return m*x
tol=1.0e-6
m,a=1.0,1.0
arln=simp13XarcLen(f,m,0,a,tol) # parameter=m
print('Arc length=',arln)