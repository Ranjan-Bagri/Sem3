from backDiffTable import *

fr=open("disFunc01.dat","r") # input data file is the discrete function
x,y=[],[]
while True:
    data=fr.readline().split()
    if not data:
        break
    x.append(float(data[0]))
    y.append(float(data[1]))
fr.close()

back_diff_tb=backDiffTable(y)
printBackDifftable(back_diff_tb)