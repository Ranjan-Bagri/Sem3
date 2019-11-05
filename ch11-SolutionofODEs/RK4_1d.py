# Fourth order Runge-Kutta method for solving 1st order differential equation
def RK4_1d(f,pr,x,y,dx,X):
    # arguments:
    # f(pr,x,y) ==> user defined function
    # pr[...,...,...] ==> optional user defined set of turnable parameters to be used in user defined function. If no parameter is required then set 'pr' value to None
    # x,y ==> initial values x and y(x)
    # dx ==> step length (in text it is h)
    # X ==> final value of x
    # returns:
    # xx ==> array of x-values
    # yy ==> array of y-values
    # ddydx ==> array of dy/dx values
    xx,yy,ddydx=[],[],[]
    while abs(x)<abs(X): # absolute values allow to go forward and the reverse direction
        k1=dx*f(pr,x,y)
        k2=dx*f(pr,x+0.5*dx,y+0.5*k1)
        k3=dx*f(pr,x+0.5*dx,y+0.5*k2)
        k4=dx*f(pr,x+dx,y+k3)
        dy=(1/6)*(k1+2*k2+2*k3+k4)
        xx.append(x)
        yy.append(y)
        ddydx.append(dy/dx)
        y+=dy
        x+=dx
    return xx,yy,ddydx