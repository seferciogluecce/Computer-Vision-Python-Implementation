import cv2

I = cv2.imread("birds.png",0)

cv2.imshow("Birds",I)


ret,B=cv2.threshold(I, 30, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresholded	at	30",B)


ret,B=cv2.threshold(I, 70, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresholded	at	70",B)


ret,B=cv2.threshold(I, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresholded	at	120",B)

cv2.waitKey(0)
cv2.destroyAllWindows()