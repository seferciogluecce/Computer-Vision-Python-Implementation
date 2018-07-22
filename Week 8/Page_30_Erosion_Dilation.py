import cv2
import numpy as np

I = cv2.imread('original.png',0)
cv2.imshow('Original',I)


J = cv2.erode(I,np.ones((3,3),np.uint8))
cv2.imshow('erosion',J)


J = cv2.dilate(I,np.ones((3,3),np.uint8))
cv2.imshow('dilation',J)



cv2.waitKey(0)
cv2.destroyAllWindows()