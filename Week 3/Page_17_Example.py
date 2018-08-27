import cv2

import numpy as np
import math

I=cv2.imread("LicensePlate.png",0) #read image
cv2.imshow("License Plate Original", I)

height,width=I.shape

M= cv2.getRotationMatrix2D((width/2,height/2),-15,1)


sin = math.sin(M[0,0])
cos = math.cos(M[0,1])
bound_w = int((height * abs(sin)) + (width * abs(cos)))
bound_h = int((height * abs(cos)) + (width * abs(sin)))

M[0, 2] += ((bound_w / 2) - width/2)
M[1, 2] += ((bound_h / 2) - height/2)

J1 = cv2.warpAffine(I,M,(bound_w,bound_h))

cv2.imshow("License Plate Rotated", J1)
cv2.waitKey(0)
cv2.destroyAllWindows()



tform=np.float32([ [1,0.3,0],[0,1,0],[0,0,1]])
J2 = cv2.warpAffine(J1,tform,(bound_w,bound_h))

cv2.imshow("License Plate Skewed", J2)

cv2.waitKey(0)
cv2.destroyAllWindows()



































