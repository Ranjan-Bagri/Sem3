# Plot surface and tangent plane
from math import * 
from derivative import dfdx3
import numpy as np 

def zPhi(x,y):
    return x**2+y**2
def zTang(x,y,x0,y0,z0,m0,m1,m2):
    # m0,m1,m2=dfdx_yz,dfdy_zx,dfdz_xy
    return z0-(x-x0)*m0/m2-(y-y0)*m1/m2
def phix(pr,x):
    [y,z]=pr
    return z-x**2-y**2
def phiy(pr,y):
    [z,x]=pr
    return z-x**2-y**2
def phiz(pr,z):
    [x,y]=pr
    return z-x**2-y**2

tol=1.0e-6
x0,y0,z0=5,3,5 # point of interest
dfdx_yz=dfdx3(phix,[y0,z0],x0,tol)
dfdy_zx=dfdx3(phiy,[z0,x0],y0,tol)
dfdz_xy=dfdx3(phiz,[x0,y0],z0,tol)

X=np.arange(x0-20,x0+20,0.8)
Y=np.arange(y0-20,y0+20,0.8)
X,Y=np.meshgrid(X,Y)
z_surf=zPhi(X,Y)
z_tang=zTang(X,Y,x0,y0,z0,dfdx_yz,dfdy_zx,dfdz_xy)

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig=plt.figure()
ax=fig.gca(projection='3d')
# Plot the tangent plane
# 'cmp' style is choosen as RdBu
# 'antialiased' is choosen so that matplotlib artist (polygon) is drawn
surf=ax.plot_surface(X,Y,z_surf,cmap=cm.RdBu,linewidth=0,antialiased=True)
tang=ax.plot_surface(X,Y,z_tang,cmap=cm.RdBu,linewidth=0,antialiased=True)
fig.colorbar(surf,shrink=0.5) # show the colorbar scaling
fig.colorbar(tang,shrink=0.5) # with size rescaled to 0.5
plt.show()