# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:42:39 2019

@author: gribja
"""

# study of Fresnel's diffraction using fresnel's integral
import scipy.special as ss
import numpy as np
import matplotlib.pyplot as plt

from fringes import fringes

def frsInts(x,y):
    u1,u2,v1,v2=np.NINF,np.Inf,-y,np.Inf # sharp edge
    #u1,u2,v1,v2=np.NINF,np.Inf,-(2.0+y),(2.0-y) # narrow slit with width =4.0
    su1,cu1=ss.fresnel(u1)
    su2,cu2=ss.fresnel(u2)
    sv1,cv1=ss.fresnel(v1)
    sv2,cv2=ss.fresnel(v2)
    ints=((cu2-cu1)**2+(su2-su1)**2)*((cv2-cv1)**2+(sv2-sv1)**2)
    return 0.25*ints

x1,x2,y1,y2=-5,5,-3,5 # screen dimension
y=np.arange(y1,y2,0.01)
ints = frsInts(None,y)
plt.plot(y,ints,'k')
plt.xlabel('y')
plt.ylabel('Intensity')
plt.title("Intensity due to Fresnel's diffraction")
fig,ax=fringes(x1,x2,y1,y2,frsInts)
plt.show()