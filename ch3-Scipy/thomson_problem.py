import numpy as np 
from scipy.optimize import minimize
import matplotlib.pyplot as plt 
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D

def pot(th_ph):
    n=int(0.5*len(th_ph))
    u=0.0
    for i in range(n-1):
        for j in range(i+1,n):
            th0,th1=th_ph[i],th_ph[j]
            ph0,ph1=th_ph[i+n],th_ph[j+n]
            r=rij(th0,ph0,th1,ph1)
            u+=1.0/r 
    return u

def rij(th0,ph0,th1,ph1): # particle to particle separation
    snth0=np.sin(th0)
    csth0=np.cos(th0)
    snth1=np.sin(th1)
    csth1=np.sin(th1)
    snph0=np.sin(ph0)
    csph0=np.cos(ph0)
    snph1=np.sin(ph1)
    csph1=np.cos(ph1)
    rij2=(snth0*csph0-snth1*csph1)**2+(snth0*snph0-snth1*snph1)**2+(csth0-csth1)**2
    return rij2**0.5

n=5 # number of particles
# arbitrary initialization
th_ph=[0.1*i for i in range(2*n)] # [0:n-1]--> theta,  [n:2n-1]--> phi
# optimization for parameters
res=minimize(pot,th_ph,method='powell',options={'xtol':1e-5,'disp':True})
th_ph=res.x 
# print the result
print(n,'particle system')

for i in range(n-1):
    for j in range(i+1,n):
        th0,th1=th_ph[i],th_ph[j]
        ph0,ph1=th_ph[i+n],th_ph[j+n]
        r=rij(th0,ph0,th1,ph1)
        print(r'%d%d=%.5f',(i,j,r)) # distances along particles

xx,yy,zz=[],[],[] # array for positions of the particles
for i in range(n):
    th,ph=th_ph[i],th_ph[i+n]
    xx.append(np.sin(th)*np.cos(ph))
    yy.append(np.sin(th)*np.sin(ph))
    zz.append(np.cos(th))

# Plotting mesh data for sphere
theta,phi=np.meshgrid(np.linspace(0.0,np.pi,100),np.linspace(0.0,2*np.pi,100))
x=np.sin(theta)*np.cos(phi)
y=np.sin(theta)*np.sin(phi)
z=np.cos(theta)

# Set colos and render
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

# Plot of Surface
ax.plot_surface(x,y,z,rstride=1,cstride=1,color='c',alpha=0.6,linewidth=0.0)

# Plot of the optimized parameters
ax.scatter(xx,yy,zz,color='k',s=20)
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
#ax.set_aspect('equal')
plt.show()