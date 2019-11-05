# Solving the equation corresponding to 2d Foucult pendulum
import numpy as np 
import matplotlib.pyplot as plt 
from coupRK4_2d import coupRK4_2d

def f1(pr,t,x,y,dxdt,dydt):
    g_l,om,cl=pr
    return -g_l*x+2*om*dydt*cl
def f2(pr,t,x,y,dxdt,dydt):
    g_l,om,cl=pr
    return -g_l*y-2*om*dxdt*cl
def exc(pr,t,x0,y0):
    # function for exact solution
    g_l,om,cl=pr
    om1=om*cl
    om2=(om1**2+g_l)**0.5
    x=x0*np.cos(om1*t)*np.cos(om2*t)+y0*np.sin(om1*t)*np.cos(om2*t)
    y=-x0*np.sin(om1*t)*np.cos(om2*t)+y0*np.cos(om1*t)*np.cos(om2*t)
    return x,y
lmb=34 # latitude in degrees
g=9.8 # acceleration due to gravity
l=3.2e6 # length of the pendulum
om=7.27e-5 # Earth's anguler velocity

lmb=lmb*np.pi/180 # degree to radian
cl=np.sin(lmb)
t0,x0,y0,dxdt0,dydt0=0,0.0,5.0,0,0 # initial conditions
tn,dt=86400,0.5 # total time=24 x 3600
pr=[g/l,om,cl]
t,sol1,sol2=coupRK4_2d(f1,f2,pr,pr,t0,x0,y0,dxdt0,dydt0,dt,tn)
plt.plot(t,sol1[0],'k',lw=0.75,markevery=10,label='x(t) calculated')
plt.plot(t,sol2[0],'k--',lw=0.75,markevery=10,label='y(t) calculated')

t=np.asarray(t)
x,y=exc(pr,t,x0,y0)
plt.plot(t,x,'k',ms=2,markevery=500,label='x(t) exact')
plt.plot(t,y,'k*',ms=2,markevery=500,label='y(t) exact')
plt.legend(loc='best',prop={'size':12})
plt.title('x and y coordinates of the Foucult pendulum')
plt.xlabel('t')
plt.show()

plt.plot(x,y,'k',lw=0.75)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Foucault pendulum precession plot')
plt.show()