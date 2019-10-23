import numpy as np 
import matplotlib.pyplot as plt 
import numpy.linalg as la 

m=[1,0.1] # mass array, number=n
k=[1,0.2,1] # Spring constants ,number =n+1
a=[1,1] # co-effeicient of superposition
n=len(k)-1 # number of masses

# construction of K-matrix
K=[]
KK=[0.0 for i in range(n)]
KK[0],KK[1]=(k[0]+k[1])/m[0],-k[1]/m[0]
K.append(KK)
for i in range(1,n-1):
    KK=[0.0 for i in range(n)]
    KK[i-1],KK[i],KK[i+1]=-k[i]/m[i],(k[i]+k[i+1])/m[i],-k[i+1]/m[i]
    K.append(KK)
KK=[0.0 for i in range(n)]
KK[n-2],KK[n-1]=-k[n-1]/m[n-1],(k[n-1]+k[n])/m[n-1]
K.append(KK)

K=np.asarray(K) # covert to ndarray
print(K)
egv,egf=la.eig(K) # get the eigen values and eigen vectors
egv=list(egv) # Python list of eigen values
egf=list(egf) # 2d python list of eigenvectors, arranged column-wise 
t,x=[],[[] for i in range(n)] # get the t and x array
tt=0 # starting time
while tt<50.0:
    t.append(tt)
    for i in range(n):
        xt=0
        for j in range(len(egf)):
            xt+=a[j]*egf[i][j]*np.cos(egv[j]**0.5*tt)
        x[i].append(xt)
    tt+=0.1

# plotting
for i in range(n):
    plt.plot(t,x[i])
    plt.title(r"$x_%d(t)$"%i)
    plt.show()
    plt.clf()