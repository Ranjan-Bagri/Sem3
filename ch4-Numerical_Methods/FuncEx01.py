import numpy as np 
def f(pr,x):
    return np.exp(pr[0]*x)*np.sin(pr[1]*x)