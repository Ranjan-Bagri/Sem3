# Solution of two coupled 2nd order differential equations of simple harmonic oscillator
import matplotlib.pyplot as plt 
from coupEuler2d import coupEuler2d

def f1(k1,t,x1,x2,dx1dt,dx2dt):
    # two parameters tunable from main
    return -k[0]*x1+k[1]*(x2-x1)
def f2(k2,t,x1,x2,dx1dt,dx2dt):
    # two parameters set from main
    return -k[0]*x2-k[1]*(x2-x1)
t=0.0
x1,dx1dt=1.0,0.00 # initial
x2,dx2dt=0.0,0.00 # conditions
dt,T=0.05,40.0
k=[10.0,1.0] # array of parameters
# get the solution of two coupled 2nd order differential equations
t,sol1,sol2=coupEuler2d(f1,f2,k,k,t,x1,x2,dx1dt,dx2dt,dt,T)
plt.plot(t,sol1[0],'k',label=r'x vs t for $k_1$')
plt.plot(t,sol2[0],'k',label=r'x vs t for $k_2$')
#plt.plot(sol1[0],sol2[0])
plt.legend(loc='best',prop={'size':12})
plt.xlabel('t')
plt.title("Solution of coupled differential equations for simple harmonic oscillator")
plt.show()