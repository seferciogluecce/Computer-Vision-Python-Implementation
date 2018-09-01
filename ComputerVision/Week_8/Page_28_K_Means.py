import numpy as np
import cv2



def KMeans(I,K):

    '''cv2.imshow('Original' ,I)'''
    
    Z = I.reshape((-1,3))
    
    # convert to np.float32
    Z = np.float32(Z)
    
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((I.shape))
    
    '''cv2.imshow('K = ' + str(K),res2)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    return res2





img = cv2.imread('road_sky.jpg')
KMeans(img,3)
cv2.imshow('K = 3', KMeans(img,3))
cv2.waitKey(0)
cv2.destroyAllWindows()