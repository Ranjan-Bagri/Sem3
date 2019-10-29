# solving of two 1st order coupled differential equations of LCR circuit
import numpy as np 
import matplotlib.pyplot as plt 
from coupEuler1d import coupEuler1d

def fx(c1,t,I1,I2):
    # array of parameters c2 is set from main
    return c1[0]+c1[1]*I1+c1[2]*I2
def fy(c2,t,I1,I2):
    # array of parameters c1 is set from main
    return c2[0]+c2[1]*I1+c2[2]*I2
t,I1,I2=0.0,0.0,0.0 # initial conditions
dt,T=0.01,10.0
c1=[6,-4,3]
c2=[3.6,-2.4,1.6]
# get solutions from euler method
t,[I1,dI1dt],[I2,dI2dt]=coupEuler1d(fx,fy,c1,c2,t,I1,I2,dt,T)
plt.plot(t,I1,'k-',label=r'Euler solution $I_1(t)$')
plt.plot(t,I2,'k--',label=r'Euler solution $I_2(t)$')
tt=np.arange(0.0,T,0.1)
# exact solution for I1(t)
I1=1.5+1.875*np.exp(-0.4*tt)-3.375*np.exp(-2*tt)
# exact solution for I2(t)
I2=2.25*np.exp(-0.4*tt)-2.25*np.exp(-2*tt)

plt.plot(tt,I1,'k.',label=r'Exact solution $I_1(t)$')
plt.plot(tt,I2,'k.',label=r'Exact solution $I_2(t)$')
plt.title('Solution of LCR circuit from Euler method')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()