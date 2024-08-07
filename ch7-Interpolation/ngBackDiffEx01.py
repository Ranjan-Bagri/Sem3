# Example of interpolation with backward difference
from ngBackDiff import ngBackDiff

fr=open("disFunc01.dat","r") # input data file is the discrete function
x,y=[],[]
while True:
    data=fr.readline().split()
    if not data:
        break
    x.append(float(data[0]))
    y.append(float(data[1]))
fr.close()

# get the interpolated value at 4.7 corresponding to zeroth row
print(ngBackDiff(x,y,4.7)) # respect to zeroth row, default