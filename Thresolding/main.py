import numpy as np
from matplotlib import pyplot as plt
import cv2

## Fotoğrafı Okuyalım -> GRAYSCALE olarak okuduk ##
img = cv2.imread("img/bart.png",0)

## Thresolding : Fotoğrafların bazı özelliklerini ön plana çıkarmamızı sağlar. Fotoğraf GRAYSCALE formatta olmalı ##

## Yöntem 1 Threshold
#  1. parametre fotoğrafımız
#  2. ve 3. parametre aralık. 127 ve 255 arasıdır. 150-200 denendi
#  4. parametre thresholding type'ını belirtir. ##
booleanValues, thresholding = cv2.threshold(img,150,200,cv2.THRESH_BINARY)

## Yöntem 2 AdaptiveThreshold
# 1. parametre fotoğrafımın kendisi
# 2. parametre maximum alacağı değer
# 3. parametre uygulanacak thresholding type'i belirtir 4,5 ve6. parametreler dökümanda girilmesi istenen değerlerdir 5-7 girilince siyah çizgiler azaldı ##
thresholding2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("ORIGINAL",img)
cv2.imshow("THRES",thresholding2)

cv2.waitKey(0)
cv2.destroyAllWindows()



