# calculation of integration over x, with y as a parameter
# Trapezoidal rule for continuous function
# \int_a^b f(pr,x,y) dx

def trpzXy(f,pr,a,b,tol,y):
    # arguments:
    # f ==> f(pr,x,y) ==> user defined function with a parameter turnable from main
    # pr ==> user parameter turnable from main
    # a ==> lower limit of definite integral
    # b ==> upper limit of definite integral
    # tol ==> tolerence
    # returns:
    # I2 ==> value of the integral
    #
    # N.B ==> Here the number of iteration(it) is calculated ,but not returned. If required then can be sent to main.
    #
    fa,fb=f(pr,a,y),f(pr,b,y)
    I1=0.0
    n=10
    h=(b-a)/n
    it=1
    while True:
        h=(b-a)/n
        I2=0.0
        for i in range(1,n):
            I2+=f(pr,a+i*h,y)
        I2=h/2*(2*I2+fa+fb)
        if abs(I2-I1)<=tol:
            break
        it+=1
        I1=I2
        n+=10
    return I2
