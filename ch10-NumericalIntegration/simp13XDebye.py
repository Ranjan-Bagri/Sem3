# Calculation and plot of Cv/(3 N K_B) for debye model
import matplotlib.pyplot as plt 
from math import *
from simp13X import simp13X 

def f(pr,x):
    return (x**4*exp(x))/(exp(x)-1)**2
tol=1.0e-5 # tolerence
x,y=[],[] # data for plotting
TbyTD=0.1 # starting value of T/T_D
while TbyTD<3.0: # loop runs till the last value of T/T_D=3.0
    TDbyT=1/TbyTD
    I=simp13X(f,None,0.0001,TDbyT,tol) # the integral
    x.append(TbyTD)
    CvbyNK=3.0*I*(TbyTD)**3 # Cv/(3 N K_B)
    y.append(CvbyNK)
    TbyTD+=0.01 # increment of TbyTD

#### Plotting #######
plt.plot(x,y,'k-')
plt.xlabel(r'$\frac{T}{T_D}$')
plt.ylabel(r'$\frac{C_v}{3NK_B}$')
plt.show()