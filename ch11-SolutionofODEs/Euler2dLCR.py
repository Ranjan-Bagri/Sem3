# Solution of the differential equation of LCR circuit
import matplotlib.pyplot as plt 
from Euler2d import Euler2d

# d2I/dt2=2*alpha*(dI/dt)-omega^2*t
def f(al,t,I,dIdt):
    return -2*pr[0]*dIdt-pr[1]*I
lnst=['k-','k--','k-.','k:'] # array of line styles
pr=[0.1,1.0] # alpha, omega^2
T,dt=17.0,0.001
i=0

while pr[0]<=1.0:
    # initial values
    t,I,dIdt=0.0,0.0,1.0
    # solution from euler equation
    t,I,dIdt,d2Idt2=Euler2d(f,pr,t,I,dIdt,dt,T)
    st="%.2f"%pr[0]
    plt.plot(t,I,lnst[i],label=r'$\alpha=$'+st)
    plt.legend(loc='best',prop={'size':12})
    plt.xlabel('x')
    plt.ylabel('y')
    pr[0]+=3.0
    i+=1
plt.show()
