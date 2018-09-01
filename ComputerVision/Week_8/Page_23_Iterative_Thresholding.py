import cv2
from matplotlib import pyplot as plt
import numpy as np


def IterativeThreshold(I,T):
    lastT=0
    while abs(T-lastT) > 1 :
        lastT=T
        mf= np.mean(I[I>T])
        mb= np.mean(I[I<=T])
        T=0.5*(mb+mf)
    

    
    ret,B=cv2.threshold(I, T, 255, cv2.THRESH_BINARY)
    '''cv2.imshow("Thresholded	at " + str(int(T)),B)'''
    return(B,T)
    

'''I = cv2.imread("lung.png",0)  #Example program
(img,threshold)= IterativeThreshold(I,50)
cv2.imshow("Thresholded	at " + str(int(threshold)),img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''