#*************
# Not Tested
#*************
import numpy as np 

def CalculateSimpleLUT(a):
    x = [i for i in range(256)]
    LUT = [ 255/(1+np.exp(-a*(j-127)/32)) for j in x]
    return LUT

#OR
def CalculateSimpleLUT_2(a):
    LUT = [ 255/(1+np.exp(-a*(x-127)/32)) for x in range(256)]
    return LUT