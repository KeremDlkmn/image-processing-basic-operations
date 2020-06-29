import numpy as np
import cv2

## Fotoğraf Okuyalım ##
img = cv2.imread("img/bart.png")

## cvtColor() Fonksiyonu ile renk uzayını değiştirmemiz sağlanır ##
## 2 parametre alır.
#  1. parametre Formatını değiştirmek istediğimiz fotoğraf
#  2. parametre çevirmek istediğimiz formatı giriyoruz ##

grayFormatImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) ## bart.jpg BGR formatındadır.(RGB renklerine sahiptir.) Bunu GRAY formata çevirmek için, cv2.COLOR_BGR2GRAY (BGR to GRAY anlamında)
cv2.imshow("GRAY",grayFormatImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

