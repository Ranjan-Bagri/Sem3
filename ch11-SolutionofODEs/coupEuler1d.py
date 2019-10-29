# Solution of two 1st order coupled differential equations by Euler method
def coupEuler1d(f1,f2,pr1,pr2,x,y1,y2,dx,X):
    # arguments:
    # f1(pr1,x,y1,y2) ==> user defined function
    # f2(pr2,x,y1,y2) ==> user defined function
    # pr1,pr2 ==> parameters
    # x,y1,y2 ==> initial values x and y(x)
    # dx ==> step length 
    # X ==> final value of x
    # returns:
    # xx ==> array of x-values
    # [[yy1] [ddy1dx]] ==> 2d arrays containing 1d arrays
    # [[yy2] [ddy2dx]]
    xx=[]
    yy1,ddy1dx=[],[]
    yy2,ddy2dx=[],[]
    while abs(x)<abs(X): # absolute values allow to go forward and the reverse direction
        dy1dx=f1(pr1,x,y1,y2)
        xx.append(x)
        yy1.append(y1)
        ddy1dx.append(dy1dx)
        dy2dx=f2(pr2,x,y1,y2)
        yy2.append(y2)
        ddy2dx.append(dy2dx)
        y1+=dy1dx*dx 
        y2+=dy2dx*dx
        x+=dx 
    return xx,[yy1,ddy1dx],[yy2,ddy2dx]