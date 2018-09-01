#*************
# Not Tested
#*************
import numpy as np

def CalculateLUT(I,J):    
    
    PI_noncumulative,edges=np.histogram([a for a in I.ravel()],256,[0,256],[0,1])
    PI=PI_noncumulative.cumsum()
    PJ_noncumulative,edges=np.histogram([a for a in J.ravel()],256,[0,256],[0,1])
    PJ=PJ_noncumulative.cumsum()
    
    LUT = np.zeros([256])
    gJ=0
    
    for gI in range(256):
        while PJ[gJ] < PI[gI] and gJ<256:
            gJ = gJ+1
        LUT[gI] = gJ
        
    return LUT