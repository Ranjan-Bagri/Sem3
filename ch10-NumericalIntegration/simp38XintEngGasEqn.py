# calculation of internal energy of any gas equation
import sys
sys.path.append('../ch9-NumericalDifferentiation')
from derivative import dfdx3
from simp38X import simp38X
from math import *
import matplotlib.pyplot as plt 

def P(pr,T):
    # pr =[V,R,a,b]
    return pr[1]*T/(pr[0]-pr[3])-pr[2]/pr[0]**2 # Vander waals
    #return pr[1]*T/(pr[0]-pr[3])-pr[2]/(T*pr[0]**2) # Berthelot
    #return pr[1]*T/(pr[0]-pr[3])-pr[2]/(T**0.5*pr[0]*(pr[0]+pr[3])) # Redlich-Kwong 

def X(pr,v):
    # pr = [T,R,a,b]
    T=pr[0]
    pr1=[v,pr[1],pr[2],pr[3]] # parameter is redefined to obtain (dP/dT)_V
    dpdT_v=dfdx3(P,pr1,T,tol) # tol is included
    p=P(pr1,T) # pressure
    return T*dpdT_v-p
print("Convergence of the integral")
tol=1.0e-4 # tolerance for calculating kderivative
R,a,b=0.08205,3.606788,0.04286 # C02 values
V,XX,XX2=[],[],[]
T=310
v=b+0.02
while v<=0.5:
    pr=[T,R,a,b]
    V.append(v)
    v0=v
    I1,m=0,100
    while True:
        I2=simp38X(X,pr,v0,m,1.0e-3)
        if abs(I2-I1)<1.0e-2: # convergence tolerance is reduced
            break
        I1=I2
        m+=10
print(I2)
XX.append(I2)
XX2.append(a/v) # exact for vander waals
#XX2.appen(2*a/(v*T)) # exact for berthelot
#XX2.append(3*a/(2*b*T**0.5)*log(1+b/v)) # Exact for redlich
v+=0.01

######### Visualization ########
plt.plot(V,XX,'k',label='Calculated')
plt.plot(V,XX2,'k*',markevery=3,label='Exact')
plt.legend(loc='best',prop={'size':12})
plt.show()