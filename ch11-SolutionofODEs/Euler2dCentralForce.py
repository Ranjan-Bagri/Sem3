# Motion under central force.
# Tracjectories are demonstrated in polar coordinates
import numpy as np 
import matplotlib.pyplot as plt 
from Euler2d import Euler2d

def fu(k,u):
    # central force f(r) = -k/r^2 ==> f(u) = -ku^2
    return -k*u**2
def f(k,th,u,dudth):
    # function with parameter k
    return -u-fu(k,u)/u**2

k=2.0
p=k-0.8*k
while p<=k+0.8*k:
    # p=k is circle
    th,dth,Th=0.0,0.01,2*np.pi
    th,u,dudth=0.0,p,0.0
    th,u,dudth,d2udth2=Euler2d(f,k,th,u,dudth,dth,Th)
    r=[1/u[i] for i in range(len(u))]
    plt.polar(th,r,label='numerical')
    th=np.arange(0,2*np.pi,0.1)
    r=1/(k+(p-k)*np.cos(th)) # analytical solutions
    plt.polar(th,r,'.',label='analytical')
    plt.legend(loc='best',prop={'size':12})
    plt.title('p=%.3f'%p)
    plt.pause(1.0)
    plt.clf()
    p+=0.2
