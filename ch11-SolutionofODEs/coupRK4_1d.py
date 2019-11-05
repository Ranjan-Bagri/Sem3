# Solution of two 1st order differential equation by rk4 method
# equatiions are ==>
# dy1/dx=f1(pr1,x,y1,y2) and dy2/dx=f2(pr2,x,y1,y2)
def coupRK_41d(f1,f2,pr1,pr2,x,y1,y2,dx,X):
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
        L1=dx*f1(pr1,x,y1,y2)
        K1=dx*f2(pr2,x,y1,y2)

        L2=dx*f1(pr1,x+0.5*dx,y1+0.5*L1,y2+0.5*K1)
        K2=dx*f2(pr2,x+0.5*dx,y1+0.5*L1,y2+0.5*K1)

        L3=dx*f1(pr1,x+0.5*dx,y1+0.5*L2,y2+0.5*K2)
        K3=dx*f2(pr2,x+0.5*dx,y1+0.5*L2,y2+0.5*K2)

        L4=dx*f1(pr1,x+dx,y1+L3,y2+K3)
        K4=dx*f2(pr2,x+dx,y1+L3,y2+K3)

        dy1=(1/6)*(L1+2*L2+2*L3+L4)
        dy2=(1/6)*(K1+2*K2+2*K3+K4)

        xx.append(x)
        yy1.append(y1)
        ddy1dx.append(dy1/dx)
        yy2.append(y2)
        ddy2dx.append(dy2/dx)
        y1+=dy1
        y2+=dy2
        x+=dx 
    return xx,[yy1,ddy1dx],[yy2,ddy2dx]