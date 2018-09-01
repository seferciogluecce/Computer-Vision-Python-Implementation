import cv2
import numpy as np

def Open(I):
    J = cv2.morphologyEx(I, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    return J

def Close(I):
    J = cv2.morphologyEx(I, cv2.MORPH_CLOSE, np.ones((3,3),np.uint8))
    return J

def OpenClose(I):
    J1 = Open(I)
    J2 = Close(J1)
    return J2

'''I = cv2.imread('original.png',0) #example program
cv2.imshow('Open',Open(I))
cv2.imshow('Close',Close(I))
cv2.imshow('Open CLose',OpenClose(I))
cv2.waitKey(0)
cv2.destroyAllWindows() '''