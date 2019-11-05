# Solution of a 2nd order two coupled differential equation by Rk4 method
# Equations are ==> 
# d2y1/dx2=f1(pr1,x,y1,y2,dy1/dx,dy2/dx)
# d2y2/dx2=f2(pr2,x,y1,y2,dy1/dx,dy2/dx)
def coupRK4_2d(f1,f2,pr1,pr2,x,y1,y2,dy1dx,dy2dx,dx,X):
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
    while abs(x)<abs(X):
        xx.append(x)
        L11=dx*dy1dx
        K11=dx*f1(pr1,x,y1,y2,dy1dx,dy2dx)

        L21=dx*dy2dx
        K21=dx*f2(pr2,x,y1,y2,dy1dx,dy2dx)

        L12=dx*(dy1dx+0.5*K11)
        K12=dx*f1(pr1,x+0.5*dx,y1+0.5*L11,y2+0.5*L21,dy1dx+0.5*K11,dy2dx+0.5*K21)

        L22=dx*(dy2dx+0.5*K21)
        K22=dx*f2(pr2,x+0.5*dx,y1+0.5*L11,y2+0.5*L21,dy1dx+0.5*K11,dy2dx+0.5*K21)

        L13=dx*(dy1dx+0.5*K12)
        K13=dx*f1(pr1,x+0.5*dx,y1+0.5*L12,y2+0.5*L22,dy1dx+0.5*K12,dy2dx+0.5*K22)

        L23=dx*(dy2dx+0.5*K22)
        K23=dx*f2(pr2,x+0.5*dx,y1+0.5*L12,y2+0.5*L22,dy1dx+0.5*K12,dy2dx+0.5*K22)

        L14=dx*(dy1dx+K13)
        K14=dx*f1(pr1,x+dx,y1+L13,y2+L23,dy1dx+K13,dy2dx+K23)

        L24=dx*(dy2dx+K23)
        K24=dx*f2(pr1,x+dx,y1+L13,y2+L23,dy1dx+K13,dy2dx+K23)

        dy1=(1/6)*(L11+2*L12+2*L13+L14)
        dy1dx1=(1/6)*(K11+2*K12+2*K13+K14)
        d2y1dx2=dy1/dx
        yy1.append(y1)
        ddy1dx.append(dy1dx)
        dd2y1dx2.append(d2y1dx2)

        dy2=(1/6)*(L21+2*L22+2*L23+L24)
        dy2dx1=(1/6)*(K21+2*K22+2*K23+K24)
        d2y2dx2=dy2/dx
        yy2.append(y2)
        ddy2dx.append(dy2dx)
        dd2y2dx2.append(d2y2dx2)
        
        y1+=dy1
        dy1dx+=dy1dx1
        y2+=dy2
        dy2dx+=dy2dx1
        x+=dx
    return xx,[yy1,ddy1dx,dd2y1dx2],[yy2,ddy2dx,dd2y2dx2]