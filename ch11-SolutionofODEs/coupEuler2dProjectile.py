# Projectile motion as 2d coupled differential equation
import numpy as np 
import matplotlib.pyplot as plt 
from coupEuler2d import coupEuler2d

def fx(pr,t,x,y,dxdt,dydt):
    return 0
def fy(g,t,x,y,dxdt,dydt):
    return -g
u,th,g=10.0,np.pi/3,9.8 # values chosen on realistic basis
t,x,y,dxdt,dydt=0.0,0.0,0.0,u*np.cos(th),u*np.sin(th)
dt,T=0.01,1.8 # value of T is choose arbitrarily
t,xx,yy=coupEuler2d(fx,fy,None,g,t,x,y,dxdt,dydt,dt,T)
plt.plot(xx[0],yy[0],'k')
plt.show()