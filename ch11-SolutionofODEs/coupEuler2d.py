# Solution of two 2nd order coupled differential equations by Euler method
# d2y1/dx2=f1(pr1,x,y1,y2,dy1/dx,dy2/dx)
# d2y2/dx2=f2(pr2,x,y1,y2,dy1/dx,dy2/dx)
def coupEuler2d(f1,f2,pr1,pr2,x,y1,y2,dy1dx,dy2dx,dx,X):
    # arguments:
    # f1(pr1,x,y1,y2,dy1dx,dy2dx) ==> user defined function
    # f2(pr2,x,y1,y2,dy1dx,dy2dx) ==> user defined function
    # pr1,pr2 ==> parameters
    # x,y1,y2,dy1dx,dy2dx ==> initial values 
    # dx ==> step length 
    # X ==> final value of x
    # returns:
    # xx ==> array of x-values
    # [[yy1] [ddy1dx] [dd2y1dx2]] ==> 2d arrays containing 1d arrays
    # [[yy2] [ddy2dx] [dd2y2dx2]]
    xx=[]
    yy1,ddy1dx,dd2y1dx2=[],[],[]
    yy2,ddy2dx,dd2y2dx2=[],[],[]
    while abs(x)<abs(X): # absolute values allow to go forward and the reverse direction
        d2y1dx2=f1(pr1,x,y1,y2,dy1dx,dy2dx)
        xx.append(x)
        yy1.append(y1)
        ddy1dx.append(dy1dx)
        dd2y1dx2.append(d2y1dx2)
        d2y2dx2=f1(pr1,x,y1,y2,dy1dx,dy2dx)
        yy2.append(y2)
        ddy2dx.append(dy2dx)
        dd2y2dx2.append(d2y2dx2)
        dy1dx+=d2y1dx2*dx
        dy2dx+=d2y2dx2*dx
        y1+=dy1dx*dx 
        y2+=dy2dx*dx
        x+=dx 
    return xx,[yy1,ddy1dx,dd2y1dx2],[yy2,ddy2dx,dd2y2dx2]