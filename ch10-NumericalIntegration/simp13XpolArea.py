# Area under any polar curve
from simp13X import simp13X
def polArea(r,pr,a,b,tol):
    # arguments:
    # f ==> r(pr,th) ==> user defined function of the polar curve with a parameter turnable from main
    # pr ==> user defined parameter turnable from main
    # a ==> lower limit of definite integral
    # b ==> upper limit of definite integral
    # tol ==> tolerence
    # returns:
    # area ==> area under the curve r(pr,th) for a <=th<=b

    def curveArea(pr,th): # for determination of area under polar curve
        return 0.5*r(pr,th)**2
    area=simp13X(curveArea,pr,a,b,tol)
    return area
