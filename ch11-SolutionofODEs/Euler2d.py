# Euler method for solving 1st order differential equation
# d2y/dx2 = f(pr,x,y,dy/dx)
# user defined function from main program should be given below as f(pr,x,y,dydx)
def Euler2d(f,pr,x,y,dydx,dx,X):
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
        dd2ydx2=f(pr,x,y,dydx)
        xx.append(x)
        yy.append(y)
        ddydx.append(dydx)
        dd2ydx2.append(dd2ydx2)
        dydx+=dd2ydx2*dx
        y+=dydx*dx 
        x+=dx 
    return xx,yy,ddydx,dd2ydx2