# plot of J_n(cos th) in polar coordinates
import numpya as np 
import matplotlib.pyplot as plt 
from legendre import recPn

n=4
for i in range(n):
    r,theta=[],[]
    th=0.0
    while th<=2.0*np.pi:
        theta.append(th)
        rr=recPn(i,np.cos(th))
        r.append(rr)
        th+=0.01
ax=plt.subplot(111,projection='polar')
ax.plot(theta,r,label=r'$P_%d(\cos \theta)$'%i)
ax.legend(loc='best',prop={'size':12})
plt.show()
plt.clf()