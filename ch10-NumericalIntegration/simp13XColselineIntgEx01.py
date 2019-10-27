# Closed line integral using Simpson 1/3 rule
from simp13XlineIntg import simp13XlineIntg
def Ax(pr,t):
    # pr=[pr0,pr1,'0' or '1']
    curve=pr[len(pr)-1]
    if curve=='0': # flag for curve 0
        xx,yy=x0(pr[0],t),y0(pr[1],t)
    elif curve=='1': # flag for curve 1
        xx,yy=x1(pr[0],t),y1(pr[1],t)
    return xx-yy

def Ay(pr,t):
    # pr=[pr0,pr1,'0' or '1']
    curve=pr[len(pr)-1]
    if curve=='0': # flag for curve 0
        xx,yy=x0(pr[0],t),y0(pr[1],t)
    elif curve=='1': # flag for curve 1
        xx,yy=x1(pr[0],t),y1(pr[1],t)
    return xx+yy

def x0(pr0,t):
    # pr0=None
    return t
def y0(pr1,t):
    # pr1=None
    return t**2
def x1(pr0,t):
    # pr0=None
    return t**2
def y1(pr1,t):
    # pr1=None
    return t
tol=1.0e-6
pr0,pr1,cur=None,None,'0' # parameters of curve x0,y0 and flag
t0,t1=0,1
fnPr=[[Ax,Ay],[x0,y0],[pr0,pr1,cur]]
I1=simp13XlineIntg(fnPr,t0,t1,tol)
pr0,pr1,cur=None,None,'1' # parameters of curve x1,y1 and flag
t0,t1=1,0
fnPr=[[Ax,Ay],[x1,y1],[pr0,pr1,cur]]
I2=simp13XlineIntg(fnPr,t0,t1,tol)
print("Closed line integral=",I1+I2)