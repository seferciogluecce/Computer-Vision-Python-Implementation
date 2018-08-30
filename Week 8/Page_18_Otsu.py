import cv2;
 
I = cv2.imread("coin.png", cv2.IMREAD_GRAYSCALE)


threshold, T = cv2.threshold(I, 0, 255, cv2.THRESH_OTSU) # otsu threshold 


# Display images.
cv2.imshow("Thresholded Image", T)
cv2.imshow("Original Image", I)
cv2.waitKey(0)
cv2.destroyAllWindows()