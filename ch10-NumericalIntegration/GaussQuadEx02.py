# calculation integral with 20 points Gaussian quadrature
from GaussQuad import GaussLegdQuad
import numpy as np 
def f(pr,x):
    # integrand
    p,q=pr
    return 1/(p+q*np.sin(x))
a,b=0,2*np.pi # limits
pr=[2.0,1.0] # parameter

print('Integral from Gaussian quadrature',GaussLegdQuad(f,pr,20,a,b))
print('Exact value of the integral',2*np.pi/(pr[0]**2-pr[1]**2)**0.5)