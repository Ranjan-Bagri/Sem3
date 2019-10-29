# solution of two coupled 1st order differential equations of projectile motion
import numpy as np 
import matplotlib.pyplot as plt 
from coupEuler1d import coupEuler1d

def fy(uy,t,x,y):
    # user defined function with parameter uy
    g=1.0 # initialy defined parameters
    return uy-g*t
def fx(ux,t,x,y):
    # user defined function with parameter ux
    return ux
u,th=1.0,np.pi/3
ux,uy=u*np.cos(th),u*np.sin(th) # initial velocities as parameters
t,x,y=0.0,0.0,0.0 # initial values
dt,T=0.01,1.7 # values taken arbitrarily
# obtain solution of coupled 1st order differential equation
t,[x,dxdt],[y,dydt]=coupEuler1d(fx,fy,ux,uy,t,x,y,dt,T)
plt.plot(x,y,'k',label='Solution of Projectile motion')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()