## Canny Fonksiyonunu kullanarak fotoğraf ve videolarda ki kenarları algılayacağız
# cv2.Canny(img,minThreshold,maxThreshold) şeklinde yazılır. ##

import numpy as np
import cv2

video = cv2.VideoCapture(0)

while(True):
    booleanValue, Frames = video.read()
    Frames = cv2.flip(Frames,1)

    edges = cv2.Canny(Frames,100,200)

    cv2.imshow("FRAME",Frames)
    cv2.imshow("EDGE",edges)

    if(cv2.waitKey(0) & 0xFF == ord('q')):
        break
video.release()
cv2.destroyAllWindows()