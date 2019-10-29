# Forced vibration without damping (m=k=F0=1)
# d2x/dt2=-x-sin(\omega t)

import numpy as np 
import matplotlib.pyplot as plt 
from Euler2d import Euler2d

def f(omg,t,x,dxdt):
    # function defined with parameter being from main
    return -x-np.sin(omg*t)
# initial values of t,x,dxdt
t,x,dxdt=0.0,0.0,0.0
dt,T=0.05,150.0
omg=0.9 # initial value of omega
while omg<=1.05:
    tt,xx,ddxdt,dd2xdt2=Euler2d(f,omg,t,x,dxdt,dt,T) # solution
    plt.title(r'$\omega=$ %.2f'%omg)
    plt.xlabel('t')
    plt.plot(tt,xx,'k',label='x')
    # derivative
    plt.plot(tt,ddxdt,'k--',label=r'$\frac{dx}{dt}$')
    plt.legend(loc='best',prop={'size':12})
    plt.show()
    omg+=0.05 # omega is varying with this increment