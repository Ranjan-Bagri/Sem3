# Solution of Newton's law of motion under damping
# d2x/dt2=a-b(dx/dt)^n
import matplotlib.pyplot as plt 
from Euler2d import Euler2d

def f(a,t,x,dxdt):
    # Here parameters are kept in a array
    # only 3rd item is changing from main
    return pr[0]-pr[1]*(dxdt)**pr[2]

lnst=['k.','k:','k--','k','k^','k*','ko']
pr=[1.0,-0.5,0.0]
t,x,dxdt=0.0,0.0,0.0
dt,T=0.01,1.0 # value of T is chosen arbitrarily

plt.title("Solution of Newton's law of motion under damping")
plt.xlabel('t')
plt.ylabel('x(t)')
for i in range(4):
    pr[2]=i # 3rd item of the array being tuned from main
    tt,xx,Adxdt,Ad2xdt2=Euler2d(f,pr,t,x,dxdt,dt,T)
    plt.plot(tt,xx,lnst[i],label=r'$\nu$='+'%d'%pr[2])
    plt.legend(loc='best',prop={'size':12})
plt.show()