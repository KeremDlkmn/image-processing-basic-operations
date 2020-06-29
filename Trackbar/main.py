import numpy as np
import cv2

def a(x):
    pass

## Siyah bir ekran oluşturalım
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("Image")

## Trackbar oluşturalım
## 1.parametre Trackbar'ın Adı
## 2.parametre hangi pencerenini üzerinde oluşacak
## 3. ve 4. parametre 0 ile 255 değerlerini alır
## 5.parametre boş geçilmemesi için hata almamak için kendimizin uydurduğu bir fonksiyondur
cv2.createTrackbar("R","Image",0,255,a)     ## RED
cv2.createTrackbar("G","Image",0,255,a)     ## GREEN
cv2.createTrackbar("B","Image",0,255,a)     ## BLUE
cv2.createTrackbar("ON-OFF","Image",0,1,a)  ## Switch ON/OFF Butonu o yüzden 0 ile 1 arasında olur
while(True):
    cv2.imshow("Image",img)
    key = cv2.waitKey(1) & 0xFF

    ## Klavyeden ESC Tuşuna Basılırsa
    if(key == 27):
        break
    R = cv2.getTrackbarPos("R","Image") ## R Trackbar'ın değerini aldık 1.parametre Trackbarın adı, 2.parametre üzerinde bulunacağı ekranın adı
    G = cv2.getTrackbarPos("G","Image") ## R Trackbar'ın değerini aldık 1.parametre Trackbarın adı, 2.parametre üzerinde bulunacağı ekranın adı
    B = cv2.getTrackbarPos("B","Image") ## R Trackbar'ın değerini aldık 1.parametre Trackbarın adı, 2.parametre üzerinde bulunacağı ekranın adı
    S = cv2.getTrackbarPos("ON-OFF","Image") ## S Trackbar'ın değerini aldık 1.parametre Trackbarın adı, 2.parametre üzerinde bulunacağı ekranın adı

    if(S == 0):
        img[:] = 0
    else:
        img[:] = [R,G,B]
cv2.destroyAllWindows()