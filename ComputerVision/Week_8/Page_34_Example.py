import cv2
import numpy as np


def AccuracySensivitySpecificity(skin,GroundTruth):
    rows,cols=skin.shape

    T=GroundTruth
    tpInd = (skin	==	255) &	(T	==	255)
    tnInd = (skin	==	0)	 &	(T	==	0)
    fpInd = (skin	==	255) &	(T	==	0)
    fnInd = (skin	==	0)	 &	(T	==	255)
    
    #part 2 next page
    tpImage =	np.zeros([rows, cols],dtype=np.uint8)
    tpImage[tpInd] =	255
    
    tnImage = np.zeros([rows, cols],dtype=np.uint8)
    tnImage[tnInd] =	255
    
    fpImage = np.zeros([rows, cols],dtype=np.uint8)
    fpImage[fpInd] = 255
    
    fnImage	=	np.zeros([rows, cols],dtype=np.uint8)
    fnImage[fnInd]	=	255
    
    '''cv2.imshow('true	positives',tpImage)
    cv2.imshow('true	negatives',tnImage)
    cv2.imshow('false	positives',fpImage)
    cv2.imshow('false	negatives',fnImage)'''
    
    tp	= len(tpInd)
    tn	= len(tnInd)	
    fp	= len(fpInd)
    fn	= len(fnInd)	
    
    #	Compute	measures	
    accuracy =	(tp	 + tn)/ (tp	 + tn + fp	+ fn)
    sens =	tp/	(tp	 + fn)
    spec =	tn/	(tn	 + fp)
    '''print('Accuracy	=	' + str(accuracy) + ',	sensitivity	=	' + str(sens) + ',	specificity	=	' +	str(spec))	   
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    return (accuracy,sens, spec),(tpImage,tnImage,fpImage,fnImage)

'''import Page_14_Skin_Segmentation as SS  #example program

I = cv2.imread("face.jpg")
T = cv2.imread("groundTruth.png",0)
skin  = SS.ChaiSkinSegmentation(I)
print(AccuracySensivitySpecificity(skin,T)[0])

cv2.imshow('true	positives',AccuracySensivitySpecificity(skin,T)[1][0])
cv2.imshow('true	negatives',AccuracySensivitySpecificity(skin,T)[1][1])
cv2.imshow('false	positives',AccuracySensivitySpecificity(skin,T)[1][2])
cv2.imshow('false	negatives',AccuracySensivitySpecificity(skin,T)[1][3])
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


