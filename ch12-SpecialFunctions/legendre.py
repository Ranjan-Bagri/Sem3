def Pn(n,x):
    # Direct determination of Legendre function
    # arguments:
    # n ==> order of the legendre function
    # x ==> point at which value of legendre function is to be determined
    # returns:
    # Ln ==> value of the nth order Legendre function at x
    def fct(n): # factorial required for legendre polynimial
        fc=1
        for i in range(1,n+1):
            fc*=i
        return fc
    m=n//2
    Ln=0
    for k in range(0,m+1):
        coef=(-1)**k*fct(2*n-2*k)/(2**n*fct(k)*fct(n-k)*fct(n-2*k))
        trm=coef*x**(n-2*k)
        Ln+=trm
    return Ln

def recPn(n,x):
    # Recursive determination of legendre function
    # arguments:
    # n ==> order of the legendre function
    # x ==> point at which value of legendre function is to be determined
    # returns:
    # Pn ==> value of the nth order Legendre function at x
    P0,P1=1,x
    if n==0:
        Pn=P0
    elif n==1:
        Pn=P1
    else:
        Pn_1,Pn_2=P1,P0
        for i in range(2,n+1):
            Pn=(2*i-1)/i*x*Pn_1-(i-1)/i*Pn_2
            Pn_2=Pn_1
            Pn_1=Pn
    return Pn
