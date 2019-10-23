from nthPolFit import nthPolFit
import matplotlib.pyplot as plt 

def f(x): # continuous function to create discrete function
    return 2.3-1.5*x+4.57*x**3-3.5*x**6

# prepare the array of x and y values
dx,X1,X2=0.1,-3,3
xx,yy=[],[]
x=X1

while x<=X2:
    xx.append(x)
    yy.append(f(x))
    x+=dx

# obtain coefficients
cfs=nthPolFit(6,xx,yy)
# printing
print("coeffs=")
for i in range(len(cfs)-1):
    print("%.3f"%cfs[i],end=',')
print("%.3f"%cfs[len(cfs)-1],end='\n')