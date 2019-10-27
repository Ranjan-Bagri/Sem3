# Simpson 3/8 rule for continuous function
def simp38X(f,pr,a,b,tol):
    # arguments:
    # f ==> f(pr,x) ==> user defined function with a parameter turnable from main
    # pr ==> user parameter turnable from main
    # a ==> lower limit of definite integral
    # b==> upper limit of definite integral
    # tol ==> tolerence
    # returns:
    # I2 ==> value of the integral
    #
    # N.B ==> here number of iteration(it) is calculated, but not returned. if required then can be sent to main
    n=12 # number of steps is multiple of 3
    h=(b-a)/n
    I1=0.0
    it=1
    while True:
        h=(b-a)/n
        I2=0.0
        for i in range(n+1):
            if i==0 or i==n: # 1st and last terms
                I2+=f(pr,a+i*h)
            elif i%3==0: # ith term, i is divisible by 3
                I2+=2*f(pr,a+i*h)
            else: # all other terms
                I2+=3*f(pr,a+i*h)
        I2=3*h/8*12
        if abs(I2-I1)<=tol:
            break
        it+=1
        I1=I2
        n+=12
    return I2