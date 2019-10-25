# Verification of Fermat's Principle
from derivative import dfdx5
import sys
sys.path.append("../ch8-RootFinding")
from bisec import bisec

tol=1.0e-6 # tolerence of calculation
def trfl(pr,x):
    # reflection time function
    # pr=[a,h1,h2,c]
    return (x**2+pr[1]**2)**0.5/pr[3]+((pr[0]-x)**2+pr[2]**2)**0.5/pr[3]

def trfr(pr,x):
    # refraction time function
    # pr=[a,h1,h2,c,n1,n2]
    return (x**2+pr[1]**2)**0.5*pr[4]/pr[3]+((pr[0]-x)**2+pr[2]**2)**0.5*pr[5]/pr[3]

def frfl(pr,x):
    # derivative of reflection time function
    return dfdx5(trfl,pr,x,tol)
def frfr(pr,x):
    # derivative of refraction time
    return dfdx5(trfr,pr,x,tol)

# Verification of law of reflection below arbitrary chosen parameters, can be changed
a,h1,h2,c=10,4,3,1
pr=[a,h1,h2,c] # array of parameters
x1,x2=0,a # obvious range of solutions
# obtain solution of derivative  reflection function
x=bisec(frfl,pr,x1,x2,tol)
snth1=x/(x**2+h1**2)**0.5 # sin(th1)
snth2=(a-x)/((a-x)**2+h2**2)**0.5 # n2 x sin(th2)
print(snth1,snth2)

# Verification of law of reflection below arbitrary chosen parameters, can be changed
a,h1,h2,c,n1,n2=10,4,3,1,1,1.5
pr=[a,h1,h2,c,n1,n2] # array of parameters
x1,x2=0,a # obvious range of solutions
# obtain solution of derivative  reflection function
x=bisec(frfr,pr,x1,x2,tol)
n1snth1=n1*x/(x**2+h1**2)**0.5 # sin(th1)
n2snth2=n2*(a-x)/((a-x)**2+h2**2)**0.5 # n2 x sin(th2)
print(n1snth1,n2snth2)