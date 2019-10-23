import sys
sys.path.append('../ch7-Interpolation/')
from bisec import bisec
from disToCnt import disToCnt
from bracSol import brackSolDis

def f(pr,x):
    # continuous function defined from discrete functionwith interpolation
    # pr[0] ==> array of x-coordinates of discrete function
    # pr[1] ==> array of y-coordinates of the discrete function
    # pr[2] ==> number of points of interpolation
    # x ==> x-coordinate where f(x) is required
    fx=disToCnt(pr[0],pr[1],x,pr[2]) # transformation to continuous function
    return fx

# get discrete function
fr=open('bisecDisMul.dat','r')
x,y=[],[]
while True:
    line=fr.readline().split()
    if not line:
        break
    x.append(float(line[0]))
    y.append(float(line[1]))
fr.close()

m=4 # number of points of interpolation
pr=[x,y,m] # array send to f(pr,x) as parameter
x0,y0=[],[] # array to collect solution points
brack=brackSolDis(x,y) # obtain the bracket of solution
for i in brack:
    xx=bisec(f,pr,x[i],x[i+1],1.0e-5) # the solutions from biesection
    x0.append(xx) # collection of x-coordinate of solution points
    y0.append(f(pr,xx)) # collection of y-coordinate of solution points

# visualization of solution
xax=[0.0 for i in range(len(x))] # y-axis
import matplotlib.pyplot as plt 
plt.plot(x,y,'k:',label='discrete function')
plt.plot(x,xax,'k--',label='x-axis')
plt.plot(x0,y0,'ko',label='roots')
plt.legend(loc='best',prop={'size':12})
plt.show()