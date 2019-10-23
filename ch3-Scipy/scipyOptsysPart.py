# Minimization of total energy of a system of particles under simultaneous attractive and repulsive potentials
from scipy.optimize import minimize
import matplotlib.pyplot as plt 

def pot(xy,l): # potential energy
    n=int(0.5*len(xy))
    u=0.0
    for i in range(n-1):
        for j in range(i+1,n):
            x0,x1=xy[i],xy[j]
            y0,y1=xy[i+n],xy[j+n]
            r=rij(x0,y0,x1,y1)
            u0=0
            # Boundary potentials
            if x0<0 or x0>l:
                u0=100
            if y0<0 or y0>l:
                u0=100
            if x1<0 or x1>l:
                u0=100
            if y1<0 or y1>l:
                u0=100
            u+=a/r**2-b/r+u0
    return u

def rij(x0,y0,x1,y1):
    rij2=(x0-x1)**2+(y0-y1)**2
    return rij2**0.5

n=6
l=1.0
a=1.0
b=0.0

while b<=30:
    xy=[0.1*i for i in range(2*n)]
    res=minimize(pot,xy,args=(l),method='powell',options={'xtol':1e-6,'disp':True})
    xy=res.x 
    x,y=[],[]
    for i in range(n):
        x.append(xy[i])
        y.append(xy[i+n])
    
    plt.scatter(x,y)
    plt.xlim([-0.1,1.1])
    plt.ylim([-0.1,1.1])
    plt.title('b=%.2f'%b)
    plt.pause(1.0)
    plt.clf()
    b+=5.0
plt.show()