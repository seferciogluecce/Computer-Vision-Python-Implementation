import cv2

cap = cv2.VideoCapture('vtest.avi')
#Read	video	frames	until	available	
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret== True:
        #Quickly	display	image		
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html