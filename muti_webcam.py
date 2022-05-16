import cv2
# set video device
vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(0)
vid3 = cv2.VideoCapture(0)
vid4 = cv2.VideoCapture(0)

while True:
    # set video read
    ret1, frame1 = vid1.read()
    ret2, frame2 = vid2.read()
    ret3, frame3 = vid3.read()
    ret4, frame4 = vid4.read()
    
    # show video
    cv2.imshow('Webcam 1', frame1)
    cv2.imshow('Webcam 2', frame2)
    cv2.imshow('Webcam 3', frame3)
    cv2.imshow('Webcam 4', frame4)
    
    # set button 'q' is exit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# clear video frame
vid1.release()
vid2.release()
vid3.release()
vid4.release()

# clear window form
cv2.destroyAllWindows()