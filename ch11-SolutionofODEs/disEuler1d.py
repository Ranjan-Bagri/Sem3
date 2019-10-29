# Euler method for discrete function
def disEuler1d(fx,x,y):
    # This method is applied only for fx[] is a function of x[] (not y)
    # arguments :
    # fx ==> array [f(x[0]),f(x[1]),..,f(x[n])]
    # x ==> array [x[0],x[1],..,x[n]]
    # y ==> initial value of y i.e y(x[k])
    # returns:
    # yy ==> array of values of solution
    # ddydx ==> array of dydx values
    xx,yy,ddydx=[],[],[]
    k,n=0,len(x)-1
    while True:
        dydx=fx[k]
        xx.append(x[k])
        yy.append(y)
        ddydx.append(dydx)
        dx=x[k+1]-x[k]
        y+=dydx*dx
        k+=1
        if k>=n:
            break
    return xx,yy,ddydx
