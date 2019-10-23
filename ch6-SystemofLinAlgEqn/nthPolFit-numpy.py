import numpy as np 
import numpy.polynomial.polynomial as poly 

x=np.arange(-3,3.1,0.1)
y=2.3-1.5*x+4.57*x**3-3.5*x**6

# use of function polyfit under numpy.polynomial.polynomial
# syntax : poly.polyfit(x,y,n)
# arguments
# x: array of x-values
# y: array of y-values
# n: degree of polynomial to be fitted

coeffs=poly.polyfit(x,y,6) # get the co-efficients
# printing
print("Coefficients: %.3f"%coeffs[0],end=',')
for i in range(1,len(coeffs)-1):
    print("%.3f"%coeffs[i],end=',')
print("%.3f"%coeffs[len(coeffs)-1])
