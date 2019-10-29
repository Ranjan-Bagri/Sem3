from imEuler1d import imEuler1d
import matplotlib.pyplot as plt 

def f(pr,x,y):
    return (1-2*x)*y**2

x,y=0.0,4.0 # initial values of x and y
dx,X=-0.01,-2.0
x1,y1,dydx1=imEuler1d(f,None,x,y,dx,X) # solution in reverse path
dx,X=0.01,3.0
x2,y2,dydx2=imEuler1d(f,None,x,y,dx,X) # solution in forward path
plt.plot(x1,y1,'k-',label=r'$-2 \leq x \leq 0$')
plt.plot(x2,y2,'k--',markevery=6,label=r'$0 \leq x \leq 3$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Concatenate the arrays x1,y1 and x2,y2 in proper way
# The first row of x1,y1 and x2,y2 is same
# But concatenating make no harm for that
# Make the reverse array for of both x1 and x2
x1.reverse()
y1.reverse()
# append arrays x2 and y2 with reversed x1 and y1
x1.extend(x2)
y1.extend(y2)
plt.plot(x1,y1,'k-',label=r'$-2 \leq x \leq 3$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.show()