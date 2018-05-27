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


PI=[]
PJ=[]

for g in range(256):
    PI.append(sum([i.tolist().count(g) for i in I])/(Hi*Wi))
    PJ.append(sum([i.tolist().count(g) for i in J])/(Hj*Wj))
    
plt.hist(PJ,256,[0,256],color = "red")

PI=np.cumsum(PI)
PJ=np.cumsum(PJ)

plt.hist(PJ,256,[0,256],color = "red")
plt.title("R Channel")
plt.show()

gj=0
print(np.sum(PJ))
for gi in range(mi,Mi):
    while gj<255 and PI[gi]<1 and PJ[gj]<PI[gi]:
        gj+=1
    K[gi]=gj

print(K)

cv2.imshow("Thresholded",K)

cv2.waitKey(0)
cv2.destroyAllWindows()