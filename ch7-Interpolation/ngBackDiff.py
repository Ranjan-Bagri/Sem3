# Newton-Gregory backward difference interpolation
from backDiffTable import backDiffTable

def ngBackDiff(x,y,xx,k=None):
    # Python function for NG backward difference interpolation
    # 
    # arguments
    # x ==> list of x-coordinate of discrete function
    # y ==> list of y-coordinate of discrete function
    # xx ==> x value at which interpolation is required
    # k ==> row index over which NG calculation will be done, default=len(y)-1
    #
    # returns
    # sum ==> interpolated value of discrete function at xx
    n=len(y)
    if k==None:
        k=n-1 # reset the optional argument k
    xh=(xx-x[k])/(x[1]-x[0]) 
    dy=backDiffTable(y) # get the backward difference table
    cf=1.0
    sum=0.0
    for i in range(k+1):
        # sum of the series of backward difference corresponding to row k
        sum += cf*dy[i][k]
        cf*=(xh+i)/(i+1) # co-efficient of the series
    return sum