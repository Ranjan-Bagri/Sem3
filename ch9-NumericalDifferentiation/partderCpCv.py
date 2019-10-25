import matplotlib.pyplot as plt 
from derivative import dfdx3 

def P(pr,T): # P ==> pressure, T ==> Absolute temparature
    # pr =[V,R,a,b]
    return pr[1]*T/(pr[0]-pr[3])-pr[2]/pr[0]**2 # vaan der waals equation for real gas
    # return pr[1]*T/pr[0] # ideal gas equation

def T(pr,V):
    # pr =[P,R,a,b]
    return pr[0]*(V-pr[3])/pr[1]+pr[2]*(V-pr[3])/(pr[1]*V**2) # vaan der waals
    # return pr[0]*V/pr[1] # Ideal gas equation

tol=1.0e-6
R,a,b=0.08205,3.6067788,0.04286
t=310
while t<=330:
    V,Cp_Cv,exCp_Cv=[],[],[]
    v=b+0.02
    while v<= 0.5:
        V.append(v)
        pr1=[v,R,a,b]
        dpdT_v=dfdx3(P,pr1,t,tol)
        p=P(pr1,t)
        pr2=[p,R,a,b]
        dTdv_p=dfdx3(T,pr2,v,tol)

        CpmCv=t*dpdT_v*(1.0/dTdv_p)
        Cp_Cv.append(CpmCv)
        exCp_Cv.append(R/(1-(2*a*(v-b)**2)/(R*t*v**3))) # exact
        v+=0.001
    plt.plot(V,Cp_Cv,'-',label='Calculated for T='+str(t)+'k')
    plt.plot(V,exCp_Cv,'.',label='Exact for T='+str(t)+'k')
    t+=10
plt.title(r"$C_p-C_v$ vs V for Van der Waals gas")
plt.legend(loc='best',prop={'size':12})
plt.xlabel("V")
plt.ylabel(r"$C_p-C_v")
plt.show()