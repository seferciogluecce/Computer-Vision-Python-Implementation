#*************
# Not Tested
#*************
import numpy as np
        
def BasicThreshold(I,T):
    Y=0
    X=0
    T=0
    B =np.zeros(I.shape,dtype=np.bool)

    for y in range(0,Y):
        for x in range(0,X):
            B[y][x]= (I[y][x]>=T)        