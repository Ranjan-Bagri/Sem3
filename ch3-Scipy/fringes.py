import numpy as np
import matplotlib.pyplot as plt
# python function to visualize fringes
def fringes(x1,x2,y1,y2,ints):
    # Arguments
    # x1,x2 ==> x-range of the screen
    # y1,y2 ==> y-range of the screen
    # ints  ==> intensity function ints(x,y)
    # Reurns
    # fig ==> matplotlib figure object
    # ax0 ==> matplotlib axes object
    dx,dy = 0.01,0.01
    x,y=np.meshgrid(np.arange(x1,x2,dx),np.arange(y1,y2,dy))
    np.seterr(divide='ignore',invalid='ignore')
    z=ints(x,y)
    fig=plt.figure()
    ax0=fig.add_subplot(111)
    im=ax0.pcolormesh(x,y,z,cmap='gray')
    fig.colorbar(im,ax=ax0)
    plt.title('fringes')
    plt.xlabel('x')
    plt.ylabel('y')
    return fig,ax0