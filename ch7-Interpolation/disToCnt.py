from LagInterpol import LagInterpol

def locate(x,xx):
    # it will return index i for which x[i]<=xx<=x[i+1]
    # if xx doesn't belong to x array, then it will return -1
    k=-1
    for i in range(len(x)-1):
        if (xx-x[i])*(xx-x[i+1])<=0:
            k=i
            break
    return k

# Discrete function to continuous function
def disToCnt(x,y,xx,m):
    j=locate(x,xx)
    if j!=-1:
        k=min(max(j-(m-1)//2,0),len(x)-m) # starting index
        yy=LagInterpol(x[k:k+m],y[k:k+m],xx) # local lagrange interpolation
    else:
        print("%f does not belong to x array"%xx)
        yy=None
    return yy