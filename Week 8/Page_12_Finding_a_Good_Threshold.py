import cv2
from matplotlib import pyplot as plt

I = cv2.imread("lung.png",0)

cv2.imshow("Lungs",I)

plt.hist(I.ravel(),bins=255)
plt.title("Histogram h(I)")
plt.show()

ret,B=cv2.threshold(I, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded	at	150",B)

cv2.waitKey(0)
cv2.destroyAllWindows()