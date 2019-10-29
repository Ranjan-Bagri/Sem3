# solving equation corresponding to R-C circuit
import matplotlib.pyplot as plt 
from Euler1d import Euler1d

def ch(pr,t,q):
    # RHS of charging differential equation
    E,R,C=pr
    return E/R-q(R*C)
def dch(pr,t,q):
    # RHS of discharging differential equation
    R,C=pr
    return -q(R*C)
E,R,C=10.0,100,1.5e-2 # current components
tn,dt=10,0.01 # final time, time increment
t0,q0=0,0 # initial condition for charging
t,q,dqdt=Euler1d(ch,[E,R,C],t0,q0,dt,tn)
plt.plot(t,q,'k-',label='charging')
t0,q0=0,C*E # initial condition for discharging
t,q,dqdt=Euler1d(dch,[R,C],t0,q0,dt,tn)
plt.plot(t,q,'k--',label='discharging')
plt.title('Charging and Discharging Curve')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()