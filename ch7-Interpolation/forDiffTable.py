# Prepare and print forward difference table of a given discrete function

def printDiffTable(tb):
    # Function to print the forward difference table
    # arguments
    # tb ==> 2d list of forward difference table
    # returns
    # None

    n=len(tb)
    for i in range(n):
        for j in range(n-i):
            if tb[j][i]!=None: # input table isn't none
                print("%.3f"%tb[j][i],end='')
        print('')
    return None


def forDiffTable(for_tb):
    # Function to obtain the forward difference table
    # arguments
    # for_tb ==> 1d list of y-values of the discrete function
    # returns
    # for_tb ==> 2d list of forward difference table
    for_tb=[for_tb]
    i=0
    while True:
        tb=[]
        for j in range(1,len(for_tb[i])):
            tb.append(for_tb[i][j]-for_tb[i][j-1])
        for_tb.append(tb)

        if (len(tb)==1):
            break
        else:
            i+=1
    return for_tb
