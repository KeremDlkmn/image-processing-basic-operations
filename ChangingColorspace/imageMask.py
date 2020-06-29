import numpy as np
import cv2

## Fotoğrafı Oku. ##
img = cv2.imread("img/bart.png")

## HSV Formata Çevir. ##
hsvFormat = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

## Mask Edilecek Renk Aralığı Belirlendi ##
upperYellow = np.array([48, 255, 255])
lowerYellow = np.array([18, 94, 150])

## Mask işleminin Yapılması ##
maskedImage = cv2.inRange(hsvFormat,lowerYellow,upperYellow)

## Orjinal Fotoğrafı Ekranda Gösterelim ##
cv2.imshow("Original Image",img)

## Maskelenmiş Görüntüyü Ekranda Gösterelim ##
cv2.imshow("Masked Image",maskedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()