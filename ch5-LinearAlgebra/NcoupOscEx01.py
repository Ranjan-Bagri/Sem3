from diagJacobiNcoupOsc import NcoupOsc
import matplotlib.pyplot as plt 

m=1 # mass of each particle (taken same to get the matrix as symmetric)
k=[1,0.1,0.1,1]
c=[1,1,1]
dt,T=0.1,50 # time range 0<=t<=T with t_i+1=t_i+dt

n=len(k)-1 # number of masses
t,x=NcoupOsc(m,k,c,dt,T)
for i in range(n):
    plt.plot(t,x[i])
    plt.title(r"$x_%d$(t)"%i)
    plt.show()
    plt.clf()