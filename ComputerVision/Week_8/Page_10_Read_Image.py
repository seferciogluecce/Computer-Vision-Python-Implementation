import cv2


def ReadGrayImage(imagePath):
    return cv2.imread(imagePath,0)

'''cv2.imshow("Birds",ReadGrayImage("birds.png"))  #example program
cv2.waitKey(0)
cv2.destroyAllWindows()'''