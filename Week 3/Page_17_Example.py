import cv2
import numpy as np
import math

def clearBlacks(img): #https://codereview.stackexchange.com/questions/132914/crop-black-border-of-image-using-numpy  answer by Divakar
    oneLayer = np.sum(img,axis=0)
    mask=oneLayer>0
    return img[field3d_mask = np.broadcast_to(field2d > 0.3, field3d.shape)]
    return img[np.ix_(mask.any(1),mask.any(0)),np.ix_(mask.any(1),mask.any(0)),np.ix_(mask.any(1),mask.any(0))]



I=cv2.imread("LicensePlate.png") #read image
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

J1=clearBlacks(J1)
cv2.imshow("License Plate Rotated", J1)


tform=np.float32([ [1,-0.3,0],[0,1,0],[0,0,1]])
    

h,w=J1.shape[:2]  #height and width values of the image
J2=np.zeros([h*2,w*2,3],dtype=np.uint8)

for y in range(len(J1)):
    for x in range(len(J1[y])):
        xx,yy,cc=np.dot(tform,[x,y,1])        
        if int(xx)>=0 and int(xx)<w and int(yy) >=0 and int(yy)<h:
            J2[y][x]=J1[int(yy)][int(xx)]

J2=clearBlacks(J2)
cv2.imshow("License Plate Skewed", J2)

cv2.waitKey(0)
cv2.destroyAllWindows()































