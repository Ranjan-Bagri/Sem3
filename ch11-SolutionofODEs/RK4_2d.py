# Fourth order Runge-Kutta method for solving 2nd order differential equation
# d2y/dx2 = f(pr,x,y,dy/dx)
# user defined function from main program should be given below as f(pr,x,y,dydx)
def RK4_2d(f,pr,x,y,dydx,dx,X):
    # arguments:
    # f(pr,x,y,dydx) ==> user defined function
    # pr[...,...,...] ==> optional user defined set of turnable parameters to be used in user defined function. If no parameter is required then set 'pr' value to None
    # x,y ==> initial values x and y(x)
    # dx ==> step length (in text it is h)
    # X ==> final value of x
    # returns:
    # xx ==> array of x-values
    # yy ==> array of y-values
    # ddydx ==> array of dy/dx values
    # dd2ydx2 ==> array of d2y/dx2 values
    xx,yy,ddydx,dd2ydx2=[],[],[],[]
    while abs(x)<abs(X): # absolute values allow to go forward and the reverse direction
        k11=dx*dydx
        k21=dx*f(pr,x,y,dydx)
        k12=dx*(dydx+0.5*k21)
        k22=dx*f(pr,x+0.5*dx,y+0.5*k11,dydx+0.5*k21)
        k13=dx*(dydx+0.5*k22)
        k23=dx*f(pr,x+0.5*dx,y+0.5*k12,dydx+0.5*k22)
        k14=dx*(dydx+k23)
        k24=dx*f(pr,x+dx,y+k13,dydx+k23)
        dy=(1/6)*(k11+2*k12+2*k13+k14)
        dy2=(1/6)*(k21+2*k22+2*k23+k24)       
        d2ydx2=dy/dx
        xx.append(x)
        yy.append(y)
        ddydx.append(dydx)
        dd2ydx2.append(d2ydx2)
        dydx+=dd2ydx2*dx
        y+=dy
        dydx+=dy2  
        x+=dx 
    return xx,yy,ddydx,dd2ydx2