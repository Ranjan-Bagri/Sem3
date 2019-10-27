# Gauss-Legendre Quadrature
import numpy as np 
import sys
sys.path.append('../ch12-SpecialFunctions/')
from legendre import recPn # get Legendre polynomial
sys.path.append('../ch8-RootFinding/')
from newtonRaphson import nr # Newton-Raphson method

def dPndx(n,x):
    # Derivative of Legendre polynomial
    return (n/(x**2-1))*(x*recPn(n,x)-recPn(n-1,x))

def nodes(n):
    # calculation of n nodes
    # degree of legendre polynomial
    roots=[]
    for i in range(n):
        x0=np.cos((np.pi*(i+1-0.25))/(n+0.5)) # initial guess
        root=nr(recPn,n,dPndx,n,x0,1000,1e-5)
        roots.append(root)
    return roots

def weights(n,xN):
    wg3=[]
    for x in xN:
        wn=2/((1-x**2)*dPndx(n,x)**2)
        wg3.append(wn)
    return wg3

def GaussLegdQuad(f,pr,N,a,b):
    # Integration by Gauss-Legendre quadrature
    # arguments:
    # f ==> f(pr,x) ==> user defined function with a parameter turnable from main
    # pr ==> user parameter turnable from main
    # N ==> number of nodes in gaussian quadrature
    # a ==> lower limit of definite integral
    # b ==> upper limit of definite integral
    # returns:
    # intg ==> value of the integral
    if N<2: # number of evaluation point is less than 2
        print('Number of evaluation points is too less, Quitting...')
        return None
    xN=nodes(N) # get nodes
    wN=weights(N,xN) # get weights
    intg=0 # integral
    for i in range(N):
        intg+=wN[i]*f(pr,0.5*(b-a)*xN[i]+0.5*(b+a))
    intg=0.5*(b-a)*intg # final value of integral
    return intg