import cv2
import numpy as np


def ThresholdWithFunction(I,T):
    ret,B=cv2.threshold(I, T, 255, cv2.THRESH_BINARY_INV)
    return B

def ThresholdWithBoolean(I,T):
    B = np.zeros((I.shape))   
    B[I<30] = 255
    return B

'''I = cv2.imread("birds.png",0)  #example program
T=30
cv2.imshow("Thresholded	at	30 Function",ThresholdWithFunction(I,T))
cv2.imshow("Thresholded	at	30 Boolean",ThresholdWithBoolean(I,T))

cv2.waitKey(0)
cv2.destroyAllWindows()'''