import cv2
import numpy as np

I = cv2.imread("face.jpg")
T = cv2.imread("groundTruth.png",0)

YUV= cv2.cvtColor(I, cv2.COLOR_RGB2YCR_CB);

U=YUV[:,:,1]
V=YUV[:,:,2]
R=I[:,:,2]
G=I[:,:,1]
B=I[:,:,0]

rows,cols,planes=I.shape

# Al-Tairi et al.
skin=np.zeros([rows,cols],dtype=np.uint8)
ind=(80	<	U)	&	(U	<	130)	&	(136	<	V)	&	(V	<=	200	)&	(V	>	U)	&	(R	>	80)	&	(G	>	30)	&	(B	>	15	)&	(abs(R-G)	>	15)
skin[ind]=255

cv2.imshow('Faces',I)
cv2.imshow('Ground Truth',T)
cv2.imshow('AL-Tairi',skin)


tpInd	=		(skin	==	255)	&	(T	==	255)
tnInd	=		(skin	==	0)	&	(T	==	0)
fpInd	=		(skin	==	255)	&	(T	==	0)
fnInd	=		(skin	==	0)	&	(T	==	255)


#part 2 next page

tpImage	=	np.zeros([rows,	cols],dtype=np.uint8)
tpImage[tpInd]	=	255

tnImage	=	np.zeros([rows,	cols],dtype=np.uint8)
tnImage[tnInd]	=	255

fpImage	=	np.zeros([rows,	cols],dtype=np.uint8)
fpImage[fpInd]	=	255

fnImage	=	np.zeros([rows,	cols],dtype=np.uint8)
fnImage[fnInd]	=	255

cv2.imshow('true	positives',tpImage)
cv2.imshow('true	negatives',tnImage)
cv2.imshow('false	positives',fpImage)
cv2.imshow('false	negatives',fnImage)

tp	=	len(tpInd)
tn	=	len(tnInd)	
fp	=	len(fpInd)
fn	=	len(fnInd)	

#	Compute	measures	
accuracy	=	(tp	+	tn)	/	(tp	+	tn	+	fp	+	fn);	
sens	=	tp	/	(tp	+	fn);	
spec	=	tn	/	(tn	+	fp);	
print('Accuracy	=	'	+str(accuracy)	+',	sensitivity	=	'	+str(sens)+	',	specificity	=	'+	str(spec));	

cv2.waitKey(0)
cv2.destroyAllWindows()
