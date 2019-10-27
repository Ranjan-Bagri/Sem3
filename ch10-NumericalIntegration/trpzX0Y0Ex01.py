from trpzX0Y0 import trpzX0Y0
def f(pr,x,y):
    return 9.0*x**3*y**2
tol=1.0e-3 # tolerence reduced for fast calculation
a1,b1,a2,b2=1,3,1,2
print(trpzX0Y0(f,None,a1,b1,a2,b2,tol))