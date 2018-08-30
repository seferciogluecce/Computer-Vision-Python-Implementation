import cv2

cap = cv2.VideoCapture('vtest.avi')
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 47.95, (1280,720))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = (255-frame) #Invert
        # write the inversed frame
        out.write(frame)       
        #Quickly	display image	using the	image command	
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
#It seems opencv is the main librray for video streaming, could not find for direct playing like implay on matlab