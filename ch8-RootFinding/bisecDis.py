import sys
sys.path.append('../ch7-Interpolation/')
from bisec import bisec
from disToCnt import disToCnt

def f(pr,x):
    # continuous function to be used by bisection method
    fx=disToCnt(pr[0],pr[1],x,pr[2])
    return fx

# get array of x and y values of the discrete function
fr=open('bisecDis.dat','r')
x,fx=[],[]
while True:
    line=fr.readline().split()
    if not line:
        break
    x.append(float(line[0]))
    fx.append(float(line[1]))
fr.close()

iroot=1 # lower index of the position of the of the root
m=5 # number of interpolating points
pr=[x,fx,m] # parameter required to convert from discrete to continuous function
xx=bisec(f,pr,x[iroot],x[iroot+1],1.0e-5) # get the solution
print('Root of the discrete function=',xx)