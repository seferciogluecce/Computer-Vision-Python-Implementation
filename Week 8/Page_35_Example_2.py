#part 2 next page

tpImage =	np.zeros([rows, cols],dtype=np.uint8)
tpImage[tpInd] =	255

tnImage = np.zeros([rows, cols],dtype=np.uint8)
tnImage[tnInd] =	255

fpImage = np.zeros([rows, cols],dtype=np.uint8)
fpImage[fpInd] = 255

fnImage	=	np.zeros([rows, cols],dtype=np.uint8)
fnImage[fnInd]	=	255

cv2.imshow('true	positives',tpImage)
cv2.imshow('true	negatives',tnImage)
cv2.imshow('false	positives',fpImage)
cv2.imshow('false	negatives',fnImage)

tp	= len(tpInd)
tn	= len(tnInd)	
fp	= len(fpInd)
fn	= len(fnInd)	

#	Compute	measures	
accuracy =	(tp	 + tn)/ (tp	 + tn + fp	+ fn)
sens =	tp/	(tp	 + fn)
spec =	tn/	(tn	 + fp)
print('Accuracy	=	' + str(accuracy) + ',	sensitivity	=	' + str(sens) + ',	specificity	=	' +	str(spec))	

cv2.waitKey(0)
cv2.destroyAllWindows()

#Same as page 34_example