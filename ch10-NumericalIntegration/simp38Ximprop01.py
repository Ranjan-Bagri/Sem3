from simp38X import simp38X
def f(n,x):
    return x**n
n=-2
m=10
tol=1.0e-5
I0=0
while True:
    I=simp38X(f,n,1,m,0.1*tol)
    if abs(I-I0)<tol:
        break
    I0=I
    m+=10
print('Value of the integral=',I)