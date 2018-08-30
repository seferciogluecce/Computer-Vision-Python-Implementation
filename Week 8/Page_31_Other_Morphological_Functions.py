import cv2;
import numpy as np;
 
I = cv2.imread("coin.png", cv2.IMREAD_GRAYSCALE)
  
threshold, T_inverse = cv2.threshold(I, 0, 255, cv2.THRESH_OTSU) # otsu threshold 
T = cv2.bitwise_not(T_inverse)

K_floodfill = T.copy()
h, w = T.shape[:2]
J = np.zeros((h+2, w+2), np.uint8)
 
cv2.floodFill(K_floodfill, J, (0,0), 255);
 
K_floodfill_inv = cv2.bitwise_not(K_floodfill)
 
K = T | K_floodfill_inv
 
# Display images.
cv2.imshow("Thresholded Image", T)
cv2.imshow("Filled Image", K)
cv2.waitKey(0)
cv2.destroyAllWindows()
#https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/


#connectedComponentswithStats yields every seperated component with information on each of them, such as size
I = cv2.imread("text.png", cv2.IMREAD_GRAYSCALE)
threshold, I = cv2.threshold(I, 0, 255, cv2.THRESH_OTSU) 

nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(I, connectivity=8)
sizes = stats[1:, -1]; nb_components = nb_components - 1
size = range(40,50)

J = np.zeros((output.shape))

for i in range(0, nb_components):
    if sizes[i] not in  size:
        J[output == i + 1] = 255

cv2.imshow("Thresholded Image", I)
cv2.imshow("Filtered Image", J)

cv2.waitKey(0)
cv2.destroyAllWindows()

#code source https://stackoverflow.com/questions/42798659/how-to-remove-small-connected-objects-using-opencv
#function source https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html

#regionprops yerine findNonZero'dan bahsedilebilir. https://docs.opencv.org/3.1.0/d1/d32/tutorial_py_contour_properties.html 6. fonksiyon

