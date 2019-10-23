# Newton-Gregory forward difference interpolation
from forDiffTable import forDiffTable

def ngForDiff(x,y,xx,k=None):
    # Python function for NG forward difference interpolation
    # 
    # arguments
    # x ==> list of x-coordinate of discrete function
    # y ==> list of y-coordinate of discrete function
    # xx ==> x value at which interpolation is required
    # k ==> row index over which NG calculation will be done, default=0
    #
    # returns
    # sum ==> interpolated value of discrete function at xx
    n=len(y)
    if k==None:
        k=0 # reset the optional argument k
    xh=(xx-x[k])/(x[1]-x[0]) 
    dy=forDiffTable(y) # get the forward difference table
    cf=1.0
    sum=0.0
    for i in range(n-k):
        # sum of the series of forward difference corresponding to row k
        sum += cf*dy[i][k]
        cf*=(xh-i)/(i+1) # co-efficient of the series
    return sum