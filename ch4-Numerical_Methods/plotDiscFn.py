import matplotlib.pyplot as plt 
fr=open('x22.prn','r')
xy=[]
while True:
    tmp=[] # empty array to collect data from single row
    line=fr.readline().split()
    if not line:
        break
    for i in range(len(line)):
        tmp.append(float(line[i]))
    xy.append(tmp)
fr.close()

print(xy)
data=[[xy[j][i] for j in range(len(xy))] for i in range(len(xy[0]))]
print(data)
plt.plot(data[0],data[1],'k.')
plt.title('Plot a data file')
plt.show()