def Jn(nn,x):
    # Direct calcilation of Bessel function
    # arguments:
    # nn ==> integer order of bessel function
    # x ==> where the bessel function is to be determined
    # returns:
    # sm ==> value of bessel function at x=x
    def fct(n):
        # supporting function for calculation of factorial
        fc=1
        for i in range(2,n+1):
            fc*=i
        return fc
    n=abs(nn) # get +ve n value
    tol=1.0e-5
    trm=x**n/(2**n*fct(n))
    sm=trm
    m=1
    while True:
        sm1=sm
        trm=-(x**2*trm)/(4*m*(m+n))
        sm+=trm
        m+=1
        if abs(sm-sm1)<tol:
            break
    if nn<0: # if n is negetive
        sm=(-1)**n*sm # J-n(x)=(-1)^n Jn(x)
    return sm 

def recJn(n,x):
    # calculation of bessel from recursive relation
    # arguments:
    # n ==> integer order of bessel function
    # x ==> at which bessel function is to be determined
    # returns:
    # Jn_1 ==> value of nth order bessel function at x=x
    if n==0:
        return Jn(0,x)
    elif n==1:
        return Jn(1,x)
    elif n>=2:
        Jn0,Jn_1=Jn(1,x),Jn(0,x)
        for i in range(2,n+1):
            Jn1=2*(i-1)/x*Jn0-Jn_1
            Jn_1=Jn0
            Jn0=Jn1
        return Jn1
    else: # if n is -ve
        Jn0,Jn1=Jn(0,x),Jn(1,x)
        for i in range(-1,n-1,-1):
            Jn_1=2*(i+1)/x*Jn0-Jn1
            Jn1=Jn0
            Jn0=Jn_1
        return Jn_1