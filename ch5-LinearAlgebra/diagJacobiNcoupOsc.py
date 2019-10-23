from math import cos
from diagJacobi import diagJacobi
from matOpr import matTrans

def NcoupOsc(m,k,c,dt,T):
    # arguments:
    # m ==> mass of each oscillator
    # k ==> array of spring constants, size=n+1,n=number of oscillators
    # c ==> array of coefficients of superpositions, size=n
    # dt ==> time interval
    # T ==> final time 0<=time<=t
    tol=1e-6 # Tolerence for jacobi transformation
    n=len(k)-1 # number of masses
    K=[] # empty list for spring constant matrix K
    # auxiliary list is initialized to build K matrix
    KK=[0.0 for i in range(n)]
    KK[0],KK[1]=(k[0]+k[1])/m, -k[1]/m 
    K.append(KK) # 0th row of K matrix
    for i in range(1,n-1):
        KK=[0.0 for i in range(n)] # auxiliary list is initialized
        KK[i-1],KK[i],KK[i+1]=-k[i]/m,(k[i]+k[i+1])/m,-k[i+1]/m 
        K.append(KK) # 1 to n-1 for K matrix
    # below nth row of K matrix
    KK=[0.0 for i in range(n)]
    KK[n-2],KK[n-1]=-k[n-1]/m,(k[n-1]+k[n])/m 
    K.append(KK)
    # below , eigen value (egv) and eigen vectors (egf) of symmetric K matrix
    kdg,egf=diagJacobi(K,tol)
    egv=[kdg[i][i] for i in range(n)] # eigen values, diagonal terms
    egf= matTrans(egf) # Transpose taken, column wise eigen vectors
    # empty lists for solutions x[0],x[1], .... of each mass
    t,x=[],[[] for i in range(n)]
    tt=0 # starting time
    while tt<T:
        t.append(tt)
        for i in range(n):
            xt=0
            for j in range(len(egf)):
                # displacement (x[0],x[1],..) vs time data
                xt+=c[j]*egf[i][j]*cos(egv[j]**0.5*tt)
            x[i].append(xt)
        tt+=dt
    return t,x