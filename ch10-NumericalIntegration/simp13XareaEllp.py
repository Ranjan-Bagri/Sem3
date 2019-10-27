# Area under ellipse
import numpy as np 
from simp13XpolArea import polArea

def r(e,th): # the ellipse
    return e/(1+e*np.cos(th))
e=0.7 # eccentricity
area = polArea(r,e,0.0,2*np.pi,1.0e-6) # parameter=e
print(area)