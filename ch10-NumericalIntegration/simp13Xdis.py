# simpson 1/3 rule for discrte function
def simp13Xdis(h,fx):
    # arguments:
    # h ==> step size
    # fx ==> array of y-values of the discrete function
    # returns:
    # I ==> value of the integral
    n=len(fx)
    I=0
    for i in range(n):
        if i==0 or i==n-1: # i 1st or last
            I+=fx[i]
        elif i%2!=0: # i odd
            I+=4*fx[i]
        else: # i even
            I+=2*fx[i]
        I=I*h/3
    return I
