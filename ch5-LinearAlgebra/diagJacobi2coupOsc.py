from diagJacobi import diagJacobi
from matOpr import matTrans
from math import cos
import matplotlib.pyplot as plt 

tol=1e-6 # tolerence of convergence of Jacobi method
k0,k1,k2=1,0.1,1
k=[[k0+k1,-k1],[-k1,k1+k2]] # k-matix

kd,x=diagJacobi(k,tol)

lmb=[kd[i][i] for i in range(len(kd))] # eigenvalues
cegf=matTrans(x) # get column wise eigenvectors
c=[1.0,1.0]
t,x=[],[[],[]]  # blank arrays for plotting

tt=0.0 # starting time
while tt<=50.0:
    t.append(tt)
    # x_0(t)
    x_0t=c[0]*cegf[0][0]*cos(lmb[0]**0.5*tt)+c[1]*cegf[0][1]*cos(lmb[1]**0.5*tt)
    x[0].append(x_0t)
    # x_1(t)
    x_1t=c[0]*cegf[1][0]*cos(lmb[0]**0.5*tt)+c[1]*cegf[1][1]*cos(lmb[1]**0.5*tt)
    x[1].append(x_1t)
    tt+=0.1

# Plotting w.r.t time
plt.plot(t,x[0])
plt.title(r"$x_0(t)$")
plt.show()
plt.plot(t,x[1])
plt.title(r"$x_1(t)$")
plt.show()