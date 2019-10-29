# Solution of radioactive decay equation
import matplotlib.pyplot as plt 
from Euler1d import Euler1d

def f(k,t,N):
    return -k*N

plt.title("Solution of radioactive decay equation")
plt.xlabel('x')
plt.ylabel('N')
dt,T=0.01,20 # value of increment of t and final value of t
k=0.3 # initial value of k
while k<1.5: # iteration over k
    t,N0=0.0,100 # ecah iteration starts with initial value
    # solution from euler method
    t,N,dNdt=Euler1d(f,k,t,N0,dt,T)
    # plot of the solution
    plt.plot(t,N,'k',label=r'k=%.2f, $N_0$ = %d'%(k,N0))
    plt.legend(loc='best',prop={'size':12})
    k+=0.3 # increment of k
plt.show()