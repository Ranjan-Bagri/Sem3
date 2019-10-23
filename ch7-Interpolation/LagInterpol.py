def LagInterpol(x,y,xx):
    # Function to calculate interpolated value by lagrange method
    # arguments
    # x ==> array of x-coordinates
    # y ==> array of y-coordinates
    # xx ==> x-value at which interpolated value is to be determined
    # 
    # returns
    # yy ==> interpolated value at xx
    if x!=None and y!=None and xx!=None:  # exclude null array
        n=len(x)
        yy=0
        for i in range(n):
            nu,de=1.0,1.0 # initialization
            for j in range(n):
                if j!=i:
                    nu*=(xx-x[j]) # iterated numerator of lagrange polynomial
                    de*=(x[i]-x[j]) # iterated denominator of lagrange polynomial
            lpol=nu/de # iterated lagrange polynomial
            yy+=y[i]*lpol # iterated interpolated value
    else: # x or y or xx is null
        yy=None
    return yy




