import cv2
import numpy as np
from matplotlib import pyplot as plt


I=cv2.imread("tony-stark.jpg",0)
J=cv2.imread("thanos.jpg",0)

Hi,Wi = I.shape
Hj,Wj = J.shape

K=np.zeros([Hi,Wi],dtype=np.uint8) 

mj=np.min(J)
Mj=np.max(J)

mi=np.min(I)
Mi=np.max(I)


Ihist,Ibins = np.histogram(I.flatten(),256,[0,256])
PI_nonnormal = Ihist.cumsum()
PI = PI_nonnormal * Ihist.max()/ PI_nonnormal.max()

Jhist,Jbins = np.histogram(J.flatten(),256,[0,256])
PJ_nonnormal = Jhist.cumsum()
PJ = PJ_nonnormal * Jhist.max()/ PJ_nonnormal.max()

print(PJ)
gj=mj

for gi in range(mi,Mi):
    print(gj,PI[gi],PJ[gj])
    while gj<255 and PI[gi]<1 and PJ[gj]<PI[gi]:
        gj = gj + 1
    K[gi]=gj


cv2.imshow("Thresholded",K)

cv2.waitKey(0)
cv2.destroyAllWindows()