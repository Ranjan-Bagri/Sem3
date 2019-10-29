# Euler method for solving 1st order differential equation
# dy/dx = f(pr,x,y)
# user defined function from main program should be given below as f(pr,x,y)
def Euler1d(f,pr,x,y,dx,X):
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
        dydx=f(pr,x,y)
        xx.append(x)
        yy.append(y)
        ddydx.append(dydx)
        y+=dydx*dx 
        x+=dx 
    return xx,yy,ddydx