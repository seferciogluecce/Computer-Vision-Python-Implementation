import cv2
import numpy as np

def Label(I):
    ret,B=cv2.threshold(I, 70, 255, cv2.THRESH_BINARY_INV)
    '''cv2.imshow("Thresholded	at	70",B)'''
    J = cv2.morphologyEx(B, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    '''cv2.imshow('Opened',J)'''
    
    labelCount, labels = cv2.connectedComponents(J)
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
    
    # cvt to BGR for display
    L = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    
    # set bachground label to black
    L[label_hue==0] = 0
    
    '''cv2.imshow('Labeled. Number of birds = ' + str(labelCount-1), L) #backgorund is also labeled    
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    return (L,labelCount-1)
    
    #source: https://stackoverflow.com/questions/46441893/connected-component-labeling-in-python

'''I = cv2.imread("birds.png",0)   #example program
(img,count)=Label(I)
cv2.imshow('Labeled. Number of birds = ' + str(count), img) 
cv2.waitKey(0)
cv2.destroyAllWindows()'''