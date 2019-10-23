def bracSol(f,pr,a,b,dx):
    # function to bracket solution for continuous function
    #
    # arguments
    # f,pr ==> function and its parameter argument
    # a,b ==> the range of solution
    # dx ==> interval of no solution
    #
    # returns
    # brack ==> bracket of solution
    brack=[]
    x=a
    while x<b:
        if f(pr,x)*f(pr,x+dx)<=0:
            brack.append(x)
        x+=dx
    return brack

def brackSolDis(x,fx):
    # function to barcket solution for discrete function
    #
    # arguments
    # x,fx ==> points of the discrete function
    # 
    # returns
    # brack ==> barcket of the solution
    n=len(x)
    brack=[]
    for i in range(n-1):
        if fx[i]*fx[i+1]<=0:
            brack.append(i)
    return brack 