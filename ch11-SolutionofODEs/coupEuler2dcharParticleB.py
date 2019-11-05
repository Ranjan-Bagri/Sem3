# Motion of a charged particle under uniform magnetic field
import matplotlib.pyplot as plt 
from coupEuler2d import coupEuler2d

def fx(pr1,t,x,ydxdt,dydt):
    return pr1*dydt
def fy(pr2,t,x,y,dxdt,dydt):
    return -pr2*dxdt
pr1=pr2=1.0 # qB/m
# initial conditions
t,x,y,dxdt,dydt=0.0,0.0,0.0,1.0,1.0
dt,T=0.001,8 # change dt from here
# get the solution from euler method
t,x,y=coupEuler2d(fx,fy,pr1,pr2,t,x,y,dxdt,dydt,dt,T)
plt.axes().set_aspect('equal')
plt.plot(x[0],y[0],'k',label='y vs x')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory of a charged particle under uniform magnetic field')
plt.show()