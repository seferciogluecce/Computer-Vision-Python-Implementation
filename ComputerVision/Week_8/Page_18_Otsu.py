import cv2

def OtsuThreshold(I):
    threshold, T = cv2.threshold(I, 0, 255, cv2.THRESH_OTSU) # otsu threshold 
    return threshold,T

'''I = cv2.imread("coin.png", cv2.IMREAD_GRAYSCALE)  #example program
threshold,T = OtsuThreshold(I)
cv2.imshow("Thresholded Image, T = " + str(threshold), T)
cv2.imshow("Original Image", I)
cv2.waitKey(0)
cv2.destroyAllWindows()'''