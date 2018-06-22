import cv2
import numpy as np

I=cv2.imread("tony-stark.jpg",0)

invGamma = 0.3 
lut = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

K= cv2.LUT(I, lut) #LUT mapping function of Python

cv2.imshow("Original",I)
cv2.imshow("K",K)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sources:
# www.learnopencv.com/applycolormap-for-pseudocoloring-in-opencv-c-python/
# www.programcreek.com/python/example/89460/cv2.LUT