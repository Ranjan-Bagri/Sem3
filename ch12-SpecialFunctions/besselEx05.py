# J0(x)=2/pi*\int_0^1 cos(xt)/sqrt(1-t^2)
import sys
sys.path.append('../ch10-NumericalIntegration/')
from simp13X import simp13X
import numpy as np 
import matplotlib.pyplot as plt 
from bessel import Jn

def f(x,t):
    return np.cos(x*t)/(1-t**2)**0.5

tol=1.0e-3
x,xx,yy1,yy2=-5.0,[],[],[]
while x<=5.0:
    xx.append(x)
    y=2/np.pi*simp13X(f,x,0,0.9999,tol)
    yy1.append(y)
    yy2.append(Jn(0,x))
    x+=0.1
plt.plot(xx,yy1,'k-',label=r'$\frac{2}{\pi} \int_0^1 \frac{\cos(xt)}{\sqrt{1-t^2}}dx$')
plt.plot(xx,yy2,'k.',label=r'$J_0(x)$',markevery=3)
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()