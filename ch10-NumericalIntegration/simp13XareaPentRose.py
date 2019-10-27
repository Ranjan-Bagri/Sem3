# Curve area under Pental Rose
# Equation of the above curve is given by r(theta)=sin(3*theta)
import numpy as np 
from simp13XpolArea import polArea
import matplotlib.pyplot as plt 

def r(pr,th):
    return np.sin(3*th)
area=polArea(r,None,0.0,np.pi/3,1.0e-6) # parameter=None
print('Area under the curve =',area)

rr,theta=[],[] # for plotting
th=0 # lower bound of theta
while th<= np.pi/3: # runs up the upper bound of theta
    theta.append(th)
    rr.append(r(None,th))
    th+=0.01 # increment of theta
plt.polar(theta,rr,'k-')
plt.show()