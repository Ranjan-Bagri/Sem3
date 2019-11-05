# Determine nodes and weights with different methods
import numpy as np 
import sys
sys.path.append('../ch12-SpecialFunctions/')
from legendre import recPn # get Legendre polynomial
sys.path.append('../ch8-RootFinding/')
from newtonRaphson import nr # Newton-Raphson method
sys.path.append('../ch6-SystemofLinAlgEqn/')
from GaussElim import GaussElim

def dPndx(n,x):
    # Derivative of Legendre polynomial
    return (n/(x**2-1))*(x*recPn(n,x)-recPn(n-1,x))

def nodes(n):
    # calculation of n nodes
    # degree of legendre polynomial
    roots=[]
    for i in range(int(n)):
        x0=np.cos((np.pi*(i+1-0.25))/(n+0.5)) # initial guess
        root=nr(recPn,n,dPndx,n,x0,1000,1e-5)
        roots.append(root)
    return roots

def weights(n,xN):
    # calculation of weights in Gauss-Legendre quadrature
    # n ==> number of nodes
    # xN ==> values of nodes
    # Method of undetermined coefficients : f(x)=x^k
    A=[]
    for i in range(int(n)):
        a=[]
        for j in range(int(n)):
            aa=xN[j]**i
            a.append(aa)
        aa=(1-(-1)**(i+1))/(i+1)
        a.append(aa)
        A.append(a)
    wg1=GaussElim(A)

    # Method of undetermined coefficients : f(x)=P_k(x)
    for i in range(int(n)):
        a=[]
        for j in range(int(n)):
            aa=recPn(i,xN[j])
            a.append(aa)
        aa=2 if i==0 else 0
        a.append(aa)
        A.append(a)
    wg2=GaussElim(A)

    # Direct method
    wg3=[]
    for x in xN:
        wn=2/((1-x**2)*dPndx(n,x)**2)
        wg3.append(wn)
    return wg1,wg2,wg3

N=5.0 # number of inputs
xN=nodes(N) # values of nodes
print(xN)
wg1,wg2,wg3=weights(N,xN) # weights from three methods
print(wg1,wg2,wg3)