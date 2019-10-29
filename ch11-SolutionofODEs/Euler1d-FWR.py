# simulation of full-wave rectifier
import numpy as np 
import matplotlib.pyplot as plt 
def f(RC,t,V): # RHS of capacitor discharging equation
    return -V/RC
def EulerFWR(f,pr,t,V,dt): # function to obtain discharging curve for full wave rectifier
    RC,om=pr
    t1=t+np.pi/(2*om)
    tt,VV=[],[]
    while True:
        dVdt=f(RC,t,V)
        tt.append(t)
        VV.append(V)
        if t>=t1 and abs(V-Vs*np.sin(om*t))<dt*20: # tolerence reduced
            break
        V+=dVdt*dt
        t+=dt
    return tt,VV
R,C,Vs=400,5e-3,10 # values of cicuit elements
RC,om=R*C,5.0
nc=3 # number of cycles
dt=0.0005 # increment
tt,VV=[],[] # for recoding time vs output voltage
t0,V0=np.pi/(2*om),Vs
t1=0
while t1<=t0: # initial phase 0<=wt<=pi/2
    VV.append(Vs*abs(np.sin(om*t1)))
    tt.append(t1)
    t1+=dt
for i in range(nc): # later phase wt>pi/2
    t,V=EulerFWR(f,[RC,om],t0,V0,dt)
    tt.extend(t)
    VV.extend(V) # capacitor discharge voltage recorded
    t1=tt[len(tt)-1] # intersecting point
    t0+=np.pi/om
    while t1<=t0:
        VV.append(Vs*abs(np.sin(om*t1))) # signal voltage recorded
        tt.append(t1)
        t1+=dt
plt.plot(tt,VV,'k-',label='Output voltage')
tt=np.asarray(tt)
plt.plot(tt,Vs*abs(np.sin(om*tt)),'k--',label='Input Voltage')
plt.ylim(-20,20)
plt.title('simulation of half-wave rectifier')
plt.legend(loc='best',prop={'size':12})
plt.xlabel(r'$\omega t$')
plt.ylabel('V(t)')
plt.show()