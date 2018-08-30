import numpy as np


PI=[] # CDF of I
PJ=[] # CDF of J


LUT = np.zeros([256])
gJ=0

for gI in range(256):
    while PJ[gJ] < PI[gI] and gJ<256:
        gJ = gJ+1
    LUT[gI] = gJ