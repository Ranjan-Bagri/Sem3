# Rocket motion
import sys
sys.path.append('../ch9-NumericalDifferentiation/')
from derivative import dfdx3
from RK4_1d import RK4_1d

def mass(pr,t):
    # mass variation with time
    m0,al=pr
    return m0-al*t
def f(pr,t,v):
    m0,al,v1,g=pr
    m=mass([m0,al],t)
    dmdt=dfdx3(mass,[m0,al],t,1e-5)
    return -g-dmdt*(v1/m)
m0,al,v1,g=5,0.3,2.0,9.8 # arbitrary values taken
t0,v0=0.0,0.0
tn,dt=5.0,0.01
pr=[m0,al,v1,g]
t,v,dvdt=RK4_1d(f,pr,t0,v0,dt,tn)

import numpy as np 
tt=np.linspace(t0,tn,30)
vv=-g*tt+v1*np.log(m0/(m0-al*tt))

import matplotlib.pyplot as plt 
plt.plot(t,v,'k',label='calculated')
plt.plot(tt,vv,'k.',label='exact')
plt.title('Velocity of rocket motion')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('t')
plt.ylabel('v(t)')
plt.show()