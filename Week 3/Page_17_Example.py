import cv2

import numpy as np
import math

def cropBorders(img,tol=0): #https://codereview.stackexchange.com/questions/132914/crop-black-border-of-image-using-numpy  answer by Divakar
    mask=img>0
    return img[np.ix_(mask.any(1),mask.any(0))]

I=cv2.imread("LicensePlate.png",0) #read image
cv2.imshow("License Plate Original", I)

height,width=I.shape[:2]

M= cv2.getRotationMatrix2D((width/2,height/2),-15,1)


sin = math.sin(M[0,0])
cos = math.cos(M[0,1])
bound_w = int((height * abs(sin)) + (width * abs(cos)))
bound_h = int((height * abs(cos)) + (width * abs(sin)))

M[0, 2] += ((bound_w / 2) - width/2)
M[1, 2] += ((bound_h / 2) - height/2)

J1 = cv2.warpAffine(I,M,(bound_w,bound_h))

J1=cropBorders(J1)
cv2.imshow("License Plate Rotated", J1)


tform=np.float32([ [1,0.3,0],[0,1,0]])
    

h,w=J1.shape[:2]  #height and width values of the image
J2=np.zeros([h*2,w*2],dtype=np.uint8)

J2 = cv2.warpAffine(J1,tform,(w*2,h*2))

J2=cropBorders(J2)
cv2.imshow("License Plate Skewed", J2)


cv2.waitKey(0)
cv2.destroyAllWindows()


#**************cleaner and color version

I=cv2.imread("LicensePlate.png") #read image
cv2.imshow("License Plate Original", I)

height,width=I.shape[:2]

# Rotate clockwise 15 degrees to align base
M= cv2.getRotationMatrix2D((width/2,height/2),-15,1)
J1 = cv2.warpAffine(I,M,(width,height))
cv2.imshow("License Plate Rotated", J1)


# Now apply a skew
tform=np.float32([ [1,0.3,0],[0,1,0]])
height,width=J1.shape[:2]  
J2=np.zeros([h,w],dtype=np.uint8)
J2 = cv2.warpAffine(J1,tform,(width,height))
cv2.imshow("License Plate Skewed", J2)


cv2.waitKey(0)
cv2.destroyAllWindows()