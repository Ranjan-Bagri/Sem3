# Direct backward difference
# Get the discrete function
x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
y=[0.0, 0.368, 0.541, 0.448, 0.293, 0.168, 0.089, 0.045, 0.021, 0.01]
xx=4.7 # x-value of interpolation
n=len(x)
h=x[1]-x[0] # interval equally spaced discrete function
p=(xx-x[n-1])/h
cf=p
k=1
yy=y[n-1]

for i in range(n,1,-1):
    backDiff_tb=[]
    for j in range(i-1):
        backDiff_tb.append(y[j+1]-y[j]) # current row of backward diff table
    yy+=cf*backDiff_tb[j]
    cf*=(p+k)/(k+1)
    k+=1
    y=backDiff_tb # y-values updated to current backward difference table
print(yy)