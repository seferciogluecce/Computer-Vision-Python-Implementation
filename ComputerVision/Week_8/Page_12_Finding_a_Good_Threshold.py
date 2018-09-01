import cv2
from matplotlib import pyplot as plt

def Threshold(I,T):
    '''cv2.imshow("Lungs",I)'''
    
    plt.hist(I.ravel(),bins=255)
    plt.title("Histogram h(I)")
    '''plt.show()'''
    
    ret,B=cv2.threshold(I, T, 255, cv2.THRESH_BINARY)
    '''cv2.imshow("Thresholded	at "+str(T),B)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    return (B,plt)
    
    
    
'''I = cv2.imread("lung.png",0)  #example program
T = 130
cv2.imshow("Thresholded	at " + str(T),Threshold(I,T)[0])
Threshold(I,T)[1].show()
cv2.waitKey(0)
cv2.destroyAllWindows()'''