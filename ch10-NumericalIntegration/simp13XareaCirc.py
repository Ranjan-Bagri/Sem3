# Area under circle
import numpy as np 
from simp13XpolArea import polArea
R=1.0 # radius of the circle
def r(a,th): # curve of circle
    return a
area = polArea(r,R,0.0,2*np.pi,1.0e-6) # parameter=R
print(area)