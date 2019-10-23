# Prepare and print backward difference table of a given discrete function
def printBackDifftable(tb):
    # Function to print the backward difference table
    # 
    # arguments
    # tb ==> 2d list of backward difference table
    # returns
    # None
    n=len(tb)
    for i in range(n):
        for j in range(n):
            if tb[j][i]!=None:
                print("%.3f"%tb[j][i],end="")
        print("")
    return None

def backDiffTable(back_tb):
    # Function to obtain backward difference table
    # 
    # Argument
    # back_tb ==> 1d list of y-values of the discrete function
    # 
    # returns
    # back_tb ==> 2d list of backward difference table
    n=len(back_tb)
    back_tb=[back_tb]
    for i in range(n-1):
        tb=[]
        for j in range(n):
            if j<=i:
                tb.append(None)
            else:
                # current difference table stored in temporary list tb
                tb.append(back_tb[i][j]-back_tb[i][j-1])
        back_tb.append(tb) # temporary list tb is appended to final table
    return back_tb
