import cv2

I = cv2.imread("birds.png",0)

cv2.imshow("Birds",I)
cv2.waitKey(0)
cv2.destroyAllWindows()