# Example of drawing Phase space
import numpy as np 
import matplotlib.pyplot as plt 
from RK4_2d import RK4_2d

def f(pr,t,th,dthdt):
    return 31.0-390.0*np.sin(th)-3.12*dthdt
t0,th0,dthdt0=0,200,10
tn,dt=5.0,0.005
t,th,dthdt,d2thdt2=RK4_2d(f,None,t0,th0,dthdt0,dt,tn)

plt.plot(th,dthdt,'k')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\frac{d\theta}{dt}$')
plt.title('plot of phase space')
plt.show()