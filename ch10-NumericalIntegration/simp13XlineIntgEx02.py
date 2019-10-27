# 2d vector field
from simp13XlineIntg import simp13XlineIntg
def Ax(pr,t):
    xx,yy=x(pr[0],t),y(pr[1],t)
    return 3*xx*yy

def Ay(pr,t):
    xx,yy=x(pr[0],t),y(pr[1],t)
    return -yy**2
def x(pr0,t):
    return t
def y(pr1,t):
    return 2*t**2

tol=1.0e-6
t0,t1=0,1
pr0,pr1=None,None
fnPr=[[Ax,Ay],[x,y],[pr0,pr1]] # formation of parameters
intg=simp13XlineIntg(fnPr,t0,t1,tol)
print("Line integral is=",intg)