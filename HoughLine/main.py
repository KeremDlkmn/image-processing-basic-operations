## Hough Line Transform çizgileri algılamamızı sağlar ##
import cv2
import numpy as np

vid = cv2.VideoCapture("resources/video.mp4")

while True:
    returnValue,frame = vid.read()
    frame = cv2.resize(frame,(640,480))

    ## Sarı çizgileri videodan ayıracağımız için hsv'de sarı renk belirle
    # hsv range for yellow şeklinde google da search edince renkler çıkıyor ##

    HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerYellow = np.array([18,94,140],np.uint8)
    upperYellow = np.array([48,255,255],np.uint8)

    ## mask yapalım ##
    mask = cv2.inRange(HSV,lowerYellow,upperYellow)     ## Sarı olan yerleri maskladık##
    edges = cv2.Canny(mask,75,250)                      ## Köşeleri Bulduk ##

    ## Çizgi olduğunu söyledik ##
    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)

    for line in lines:
        (x1,y1,x2,y2) = line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)


    cv2.imshow("mask",frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()