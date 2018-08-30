import cv2
import numpy as np

I = cv2.imread('original.png',0)
cv2.imshow('Original',I)


J = cv2.morphologyEx(I, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
cv2.imshow('opening',J)


J = cv2.morphologyEx(I, cv2.MORPH_CLOSE, np.ones((3,3),np.uint8))
cv2.imshow('closing',J)

K = np.ones((3,3),np.uint8)
J1 = cv2.morphologyEx(I, cv2.MORPH_OPEN, K)
J2 = cv2.morphologyEx(J1, cv2.MORPH_CLOSE, K)
cv2.imshow('opening-closing',J2)


cv2.waitKey(0)
cv2.destroyAllWindows()