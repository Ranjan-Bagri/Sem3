from simp13XareaTwoCurves import getArea
import numpy as np 
import matplotlib.pyplot as plt 
def f1(pr0,x): # 1st curve
    return x**4-2*x**2
def f2(pr1,x): # 2nd curve
    return 2*x**2
tol=1.0e-6
x0,x1,dx=-3,3,0.1 # range of judgement with increment
# obtain the intersections and the area for the curves with parameters None
insc,area=getArea(f1,None,f2,None,x0,x1,dx,tol)
print("Common area under the curve=",area)
arins=np.asarray(insc)
x=np.arange(x0,x1,dx) # get the x-value
y1=f1(None,x) # y-values for 1st curve
y2=f2(None,x) # y-values for 2nd curve
y3=f1(None,arins) # y-values of intersections
plt.plot(x,y1,'k-',label=r'$x^4-2x^2$')
plt.plot(x,y2,'k--',label=r'$2x^2$')
plt.plot(arins,y3,'ko',label='Intersections')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.show()