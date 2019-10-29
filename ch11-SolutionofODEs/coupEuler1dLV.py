# Lotka-Volterra prey-predator model
import matplotlib.pyplot as plt 
from coupEuler1d import coupEuler1d

def fx(pr1,t,x,y):
    return pr1[0]*x-pr1[1]*x*y
def fy(pr2,t,x,y):
    return -pr2[0]*y+pr2[1]*x*y
pr1=[2/3,4/3] # alpha,beta
pr2=[1,1] # gamma, delta
# plot of dx/dt and dy/dt
dt,T=0.001,20 # time separation and ultimate time
x0y0=0.9
while x0y0<2.0:
    t,x,y=0.0,x0y0,x0y0 # initial conditions
    # get the solution from coupled euler method
    tt,[xx,dxdt],[yy,dydt]=coupEuler1d(fx,fy,pr1,pr2,t,x,y,dt,T)
    # Visualization of the population of preys/predators vs t are given below
    plt.plot(tt,xx,'k',label='population of prey')
    plt.plot(tt,yy,'k--',label='population of predator')
    # the rate of increse/decrese of preys/predators can be observed by commenting in following two lines.
    #plt.plot(tt,dxdt,'k',label="Rate of Prey")
    #plt.plot(tt,dydt,'k--',label="Rate of Predator")
    tl='Initial conditions x(%.2f)=%.2f,y(%.2f)=%.2f'%(t,x,t,y)
    plt.title(tl)
    plt.legend(loc='best',prop={'size':12})
    plt.xlabel('t')
    plt.show() # switch to plot for next initial condition
    plt.clf()
    x0y0+=0.3
# Plot of y vs x
dt,T=0.0001,10
x0y0=0.9
while x0y0<2.0:
    t,x,y=0.0,x0y0,x0y0 
    tt,[xx,dxdt],[yy,dydt]=coupEuler1d(fx,fy,pr1,pr2,t,x,y,dt,T)
    lb='x(%.2f)=%.2f,y(%.2f)=%.2f'%(t,x,t,y)
    plt.plot(xx,yy,'k',label=lb)
    plt.title("Preys vs Predators")
    plt.legend(loc='best',prop={'size':12})
    plt.xlabel('x')
    plt.ylabel('y')
    plt.pause(0.5)
    x0y0+=0.3
plt.show()