# Motion under gravity
import matplotlib.pyplot as plt 
from coupEuler2d import coupEuler2d

def fx(GM,t,x,y,dxdt,dydt):
    return -GM*x/(x**2+y**2)**1.5
def fy(GM,t,x,y,dxdt,dydt):
    return -GM*y/(x**2+y**2)**1.5
GM=1
dt,T=0.05,80 # change dt from here
plt.title('Locus of a particle under gravity obtained from Euler method')
plt.xlabel('x')
plt.ylabel('y')

p=[0.5,1.0,1.5]
for dydt in p:
    t,x,y,dxdt=0.0,1.0,0.0,0.0
    # get the solution from euler method
    t,x,y=coupEuler2d(fx,fy,GM,GM,t,x,y,dxdt,dydt,dt,T)
    #plt.axes().set_aspect('equal') # for equal aspect ratio
    plt.plot(x[0],y[0],'k',label=r'y vs x for $v_y=%.2f$'%dydt)
    plt.legend(loc='best',prop={'size':12})
    plt.show()