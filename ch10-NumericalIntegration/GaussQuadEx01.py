# calculation integral with 20 points Gaussian quadrature
from GaussQuad import GaussLegdQuad
import numpy as np 
def f(pr,x):
    # integrand
    p,q=pr
    return 1/(p+q*np.sin(x))**2
a,b=0,2*np.pi # limits
p,q=2,1

print('Integral from Gaussian quadrature',GaussLegdQuad(f,[p,q],20,a,b))
print('Exact value of the integral',2*np.pi*p/(p**2-q**2)**1.5)