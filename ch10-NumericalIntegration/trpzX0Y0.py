# Calculation of definite 2d integral with fixed limits
from trpzXy import trpzXy
def trpzX0Y0(f,pr,a1,b1,a2,b2,tol):
    # arguments:
    # f ==> f(pr,x,y) ==> user defined with parameter turnable from main
    # pr ==> turnable parameter to used in functionf
    # a1 ==> user defined function as lower limit of the integral over x
    # b1 ==> user defined function as upper limit of the integral over x
    # a2 ==> lower limit of the integral over y
    # b2 ==> upper limit of the integral over y
    # returns:
    # I2 ==> value of the integral
    fa,fb=trpzXy(f,pr,a1,b1,tol,a2),trpzXy(f,pr,a1,b1,tol,b2)
    n=10
    I1=0.0
    it=1
    while True:
        h=(b2-a2)/n
        I2=0.0
        for i in range(n):
            I2+=trpzXy(f,pr,a1,b1,tol,a2+i*h)
        I2=h/2*(2*I2+fa+fb)
        if abs(I2-I1)<=tol:
            break
        it+=1
        I1=I2
        n+=10
    return I1