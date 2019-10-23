# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:12:14 2019

@author: gribja
"""

import numpy as np
from scipy.optimize import least_squares

def fnc(a,x):
    return a[0]**x**1.5*np.exp(a[1]*x)
def fit(a,f,x,fx):
    return f(a,x)-fx

fr=open('fitData.prn','r')
x,fx=[],[]

while True:
    line=fr.readline()
    if not line:
        break
    x.append(float(line.split()[0]))
    fx.append(float(line.split()[1]))
fr.close()

x=np.asarray(x)
fx=np.asarray(fx)
a=np.array([1,1])
res=least_squares(fit,a,args=(fnc,x,fx))
a=res.x
print('Fitting parameters=',a)

import matplotlib.pyplot as plt
plt.plot(x,fx,'k.',label="Data")
xx=np.arange(x[0],x[len(x)-1],0.01)
plt.plot(xx,fnc(a,xx),'k--',label="Fitted curve")
plt.legend(loc="best",prop={'size':12})
plt.title('Curve fitting by Least Square Method')
plt.show()
