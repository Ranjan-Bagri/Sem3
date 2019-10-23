import matplotlib.pyplot as plt 
from derivative import deriv 

def f(pr,x):
    for i in range(len(pr[0])):
        xx=pr[0][i]
        if abs(xx-x)<1.0e-10: # to verify that both xx and x contain same data
            yy=pr[1][i]
            break
    return yy # return the item of the 2nd column

# Get the array of data file
fr=open('x22.prn','r')
x,y=[],[]
while True:
    xy=fr.readline().split()
    if not xy:
        break
    x.append(float(xy[0]))
    y.append(float(xy[1]))
fr.close()

#parameter is array of two columns of the data file
pr=[x,y]
# h is the difference between two consecutive x-values of evenly separated array of x-values
h=x[1]-x[0]
lnx=len(x)
dy=[]

for i in range(lnx-1):
    dy.append(deriv(f,pr,x[i],h))

plt.plot(x[:lnx-1],y[:lnx-1],'k.',label='f(x)')
plt.plot(x[:lnx-1],dy,'k*',label=r'$\frac{df}{dx}$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.title('Plot of a discrete function and its derivative')
plt.show()