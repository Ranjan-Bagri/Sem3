# Simpson 1/3 rule for continuous function
def simp13X(f,pr,a,b,tol):
    # arguments:
    # f ==> f(pr,x) ==> user defined function with a parameter turnable from main
    # pr ==> user defined parameter turnable from main
    # a ==> lower limit of definite integral
    # b ==> upper limit of definite integral
    # tol ==> tolerence
    # returns:
    # I2 ==> value of the integral
    #
    # N.B ==> Here the number of iteration(it) is calculated ,but not returned. If required then can be sent to main.
    n=10
    I1=0.0
    it=1
    while True:
        h=(b-a)/n
        I2=0.0
        for i in range(n+1):
            if i==0 or i==n: # 1st and last terms
                I2+=f(pr,a+i*h)
            elif i%2==0: # even terms
                I2+=2*f(pr,a+i*h)
            else: # odd terms
                I2+=4*f(pr,a+i*h)
        I2=h/3*I2
        if abs(I2-I1)<=tol:
            break
        else:
            it+=1
            I1=I2
            n+=10
    return I2