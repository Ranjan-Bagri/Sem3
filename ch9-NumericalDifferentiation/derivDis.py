# ist order differentiation of the user defined discrete functoion
# arguments
# x,fx ==> user defined discrete function (array of x and f(x) coordinates)
# xx ==> x-value (belong to x-array) where derivative is to be determined
# returns
# dfdx ==> derivative at xx
#
def dfdx1Dis(x,fx,xx):
    n=len(x)
    k=0
    for i in range(n):
        if abs(xx-x[i])<=1.0e10:
            k=i # index of xx
            break
    if k==0: # if xx not belongs to x-array then return None
        return None
    if k!=n-1: # k is not the end point , forward difference
        dfdx=(fx[k+1]-fx[k])/(abs(x[k+1]-x[k-1]))
    else: # k is end point, backward difference
        dfdx=(fx[k]-fx[k-1])/abs(x[k]-x[k-1])
    return dfdx

def dfdx3Dis(x,fx,xx):
    n=len(x)
    k=0
    for i in range(n):
        if abs(xx-x[i])<=1.0e10:
            k=i # index of xx
            break
    if k==0: # if xx not belongs to x-array then return None
        return None
    if k>=1 and k<=n-2: # 3-point for-diff possible 1<=k<=n-2
        dfdx=(fx[k+1]-fx[k-1])/(abs(x[k+1]-x[k-1]))
    else:  # 3-point for-diff not possible
        print("3 point central difference is not possible")
    return dfdx

def dfdx5Dis(x,fx,xx):
    n=len(x)
    k=0
    for i in range(n):
        if abs(xx-x[i])<=1.0e10:
            k=i # index of xx
            break
    if k==0: # if xx not belongs to x-array then return None
        return None
    if k>=2 and k<=n-3: # 5-point for-diff possible 2<=k<=n-3
        dfdx=(fx[k-2]-8*fx[k-1]+8*fx[k+1]-fx[k+2])/(3*(abs(x[k+2]-x[k-2])))
    else:  # 5-point for-diff not possible
        print("5 point central difference is not possible")
    return dfdx