def bisec(f,pr,a,b,tol):
    # function to determine the solution by bisection method
    # 
    # arguments
    # f,pr ==> function with its parameter
    # a,b ==> range of solution
    # tol ==> tolerence of solution
    #
    # returns 
    # x ==> solution

    if f(pr,a)*f(pr,b)>0:
        print("f(a)f(b) < 0 is not satisfied in [a,b]")
        return None
    while abs(b-a)>tol:
        x=(a+b)/2.0
        if f(pr,a)*f(pr,x)<0:
            b=x
        elif f(pr,a)*f(pr,x)>0:
            a=x
        else:
            # accidentally obtained solution
            # either 'a' or 'x' or both are the solutions. It will return any one of them.
            if f(pr,a)==0.0:
                x=a
            break
    return x    