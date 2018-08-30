import cv2
import numpy as np

I=cv2.imread("tony-stark.jpg",0)
J=cv2.imread("thanos.jpg",0)

cv2.imshow("Original Image",I)
cv2.imshow("Target Image",J)

Hi,Wi = I.shape
Hj,Wj = J.shape

K=np.zeros([Hi,Wi],dtype=np.uint8) 

mj=np.min(J)
Mj=np.max(J)

mi=np.min(I)
Mi=np.max(I)

PI_noncumulative,edges=np.histogram([a for a in I.ravel()],256,[0,256],[0,1])
PI=PI_noncumulative.cumsum()
PJ_noncumulative,edges=np.histogram([a for a in J.ravel()],256,[0,256],[0,1])
PJ=PJ_noncumulative.cumsum()

gj=mj
for gi in range(mi,Mi):
    while gj<256 and PI[gi]<1 and PJ[gj]<PI[gi]:
        gj = gj + 1
    K[I==gi]=gj

cv2.imshow("Remapped Image",K)

cv2.waitKey(0)
cv2.destroyAllWindows()