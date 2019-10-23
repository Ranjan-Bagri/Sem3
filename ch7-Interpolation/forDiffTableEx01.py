# Example of use of forward difference table
# Here a discrete function ,kept in a data file is assigned in an array
# functions associated with forward difference table is imported

from forDiffTable import *
# save the data of the discrete function in a array
fr=open("disFunc01.dat","r") # input data file is the discrete function
x,y=[],[]
while True:
    data=fr.readline().split()
    if not data:
        break
    x.append(float(data[0]))
    y.append(float(data[1]))
fr.close()

forDiff_tb=forDiffTable(y) # get forward difference table
printDiffTable(forDiff_tb) # print forward difference table