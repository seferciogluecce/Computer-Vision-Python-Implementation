import cv2

import numpy as np


I=cv2.imread("LicensePlate.png",0) #read image
cv2.imshow("License Plate Original", I)

rows,cols=I.shape


M= cv2.getRotationMatrix2D((cols/2,rows/2),-15,1)
J1 = cv2.warpAffine(I,M,(cols*2,rows*2))

cv2.imshow("License Plate Rotated", J1)


tform=np.float32([ [1,0.3,0],[0,1,0],[0,0,1]])

J2 = cv2.warpAffine(J1,tform,(cols*2,rows*2))

cv2.imshow("License Plate Skewed", J2)

cv2.waitKey(0)
cv2.destroyAllWindows()