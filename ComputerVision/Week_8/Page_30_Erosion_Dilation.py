import cv2
import numpy as np


def Erosion(I):
    J = cv2.erode(I,np.ones((3,3),np.uint8))
    return J

def Dilation(I):
    J = cv2.dilate(I,np.ones((3,3),np.uint8))
    return J


'''I = cv2.imread('original.png',0)   #example program
cv2.imshow('dilation',Dilation(I))
cv2.imshow('erosion',Erosion(I))
cv2.waitKey(0)
cv2.destroyAllWindows()'''