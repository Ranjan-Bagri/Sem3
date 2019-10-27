from simp13XlineIntg import simp13XlineIntg
def Ax(pr,t):
    # pr = [pr0,pr1,pr2]
    xx,yy,zz=x(pr[0],t),y(pr[1],t),z(pr[2],t)
    return 3*xx**2+6*yy

def Ay(pr,t):
    # pr = [pr0,pr1,pr2]
    xx,yy,zz=x(pr[0],t),y(pr[1],t),z(pr[2],t)
    return -14*yy*zz
def Az(pr,t):
    # pr = [pr0,pr1,pr2]
    xx,yy,zz=x(pr[0],t),y(pr[1],t),z(pr[2],t)
    return 20*xx*zz**2
def x(pr0,t):
    return t
def y(pr1,t):
    return t**2
def z(pr2,t):
    return t**3
tol=1.0e-6
t0,t1=0,1
pr0,pr1,pr2=None,None,None 
fnPr=[[Ax,Ay,Az],[x,y,z],[pr0,pr1,pr2]] # formation of parameters
intg=simp13XlineIntg(fnPr,t0,t1,tol)
print("Line integral is=",intg)