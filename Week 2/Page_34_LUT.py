import numpy as np 

a = 2
x = [i for i in range(256)]
LUT = [ 255/(1+np.exp(-a*(j-127)/32)) for j in x]

#OR

a = 2
LUT = [ 255/(1+np.exp(-a*(x-127)/32)) for x in range(256)]