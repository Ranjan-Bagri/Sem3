import matplotlib.pyplot as plt 
from bisec import bisec

def f(pr,x):
    # f(x) = |2x-1|-5 is defined with python function
    # parameter 'pr' choosen as none from the main
    xx=2*x-1
    if xx>=0:
        fx=xx-5
    else:
        fx=-xx-5
    return fx

pr=None # parameter
a,b=0,5 # the bound of root [a,b]
rt=bisec(f,pr,a,b,1.0e-8) # tolerence is 1e-8
print(rt)

######### For Visualization #############
x,fx=[],[]
xx=0.0
while xx<=5.0:
    x.append(xx)
    fx.append(f(pr,xx))
    xx+=0.01
plt.plot(x,fx,'k',label='f(x)')
plt.plot(rt,f(pr,rt),'k*',label='root')
plt.legend(loc='best',prop={'size':12})
plt.show()