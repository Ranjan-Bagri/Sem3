# Solving equtions of motion corresponding to double pendulum
import matplotlib.pyplot as plt 
import numpy as np 
from coupRK4_2d import coupRK4_2d

def f2(pr,t,th1,th2,dth1dt,dth2dt):
    m1,m2,L1,L2,g=pr
    al=m2*L2*np.cos(th1-th2)/((m1+m2)*L1)
    be=(m2*L2*dth2dt**2*np.sin(th1-th2))+(m1-m2)*g*np.sin(th1)/((m1+m2)*L1)
    gm=(be*L1*np.cos(th1-th2)+L1*dth1dt**2*np.sin(th1-th2)-g*np.sin(th2))/(L2-al*L1*np.cos(th1-th2))
    return gm

def f1(pr,t,th1,th2,dth1dt,dth2dt):
    m1,m2,L1,L2,g=pr
    al=m2*L2*np.cos(th1-th2)/((m1+m2)*L1)
    be=(m2*L2*dth2dt**2*np.sin(th1-th2)+(m1+m2)*g*np.sin(th1))/((m1+m2)*L1)
    d2th2dt2=f2(pr,t,th1,th2,dth1dt,dth2dt)
    return -al*d2th2dt2-be
m1,m2,L1,L2,g=1,2,1,2,9.8 # data for double pendulum
pr=[m1,m2,L1,L2,g]

t0,th10,th20,dth1dt0,dth2dt0=0,0.785,1.05,0,0 # initial conditions
tn,dt=3.612,0.01
t,sol1,sol2=coupRK4_2d(f1,f2,pr,pr,t0,th10,th20,dth1dt0,dth2dt0,dt,tn)
t=np.asarray(t)
th1=np.asarray(sol1[0])
th2=np.asarray(sol2[0])

x1=L1*np.sin(th1)
y1=L1*np.cos(th1)

x2=x1+L2*np.sin(th2)
y2=y1+L2*np.cos(th2)

y1=L1+L2-y1 # shift y-coordinates for proper visualization
y2=L1+L2-y2

# plot the data
plt.plot(t,th1,'k',label=r'$\theta_1$')
plt.plot(t,th2,'k--',label=r'$\theta_2$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('t')
plt.show()
# Dynamical displacements of the pendulums
for i in range(len(t)):
    plt.title('t=%.2f'%t[i])
    plt.axis([-3,3,-0.2,3])
    plt.plot(x1[i],y1[i],'k.',ms=10,label=r'$m_1$')
    plt.plot(x2[i],y2[i],'k.',ms=10,label=r'$m_2$')
    plt.plot(x1[:i],y1[:i],'k.',ms=1,label=r'$m_1$ path, $y_1$')
    plt.plot(x2[:i],y2[:i],'k.',ms=1,label=r'$m_2$ path, $y_2$')
    plt.legend(loc='best',prop={'size':12})
    plt.xlabel(r'$x_1,x_2$')
    plt.pause(0.005)
    plt.clf()
plt.show()