import numpy as np
import cv2
#cap = cv2.VideoCapture('/home/aniruddha/Documents/Aries/Workshops/Workshop1_Image_Processing/Data/#video.mp4')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
