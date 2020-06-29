import numpy as np
import cv2

## Smoothing Images: Fotoğraflar üzerinde ki gürültüleri, pürüzleri gidermeyi amaçlayacağız ##

## Fotoğrafları Okuyalım ##
imgFilter    = cv2.imread("img/filter.png")
imgMedian    = cv2.imread("img/median.png")
imgBilateral = cv2.imread("img/bilateral.png")

## cv2.blur() : 2 parametre alır
#  1.parametre hangi fotoğrafa uygulayacağımız
#  2.parametre blur(bulanıklık) seviyesinin ne olacağı (5,5) bulanıklık seviyesidir. (pozitif tek sayı olması gerekiyor)
#  arttırdıkça fotoğraf daha da bulanıklaşır ##
blurImage = cv2.blur(imgFilter,(5,5))

## Gaussian Blur Fonksiyonu:
# 1.parametre uygulanacak fotoğraf
# 2.parametre blur seviyesi
# 3.parametre kenarlık belirtir. ##
gaussanBlurImage = cv2.GaussianBlur(imgFilter,(5,5),cv2.BORDER_DEFAULT)

## Median Blur
# 1.parametre uygulanacak olan fotoğraf
# 2.parametre bulanıklık seviyesi 5 şeklinde verilir. (pozitif tek sayılar olması gerekir) ##
medainBlur = cv2.medianBlur(imgMedian,7)

## Bilateral fonksiyonu Fotoğraf üzerinde ki pürüzleri giderir
# 1. parametre uygulanacak fotoğraf
# 2, 3 ve 4. parametre piksel dönüşüm değeridir. ##
bilateralFun = cv2.bilateralFilter(imgBilateral,7,75,75)

## Original Image ##
cv2.imshow("original", imgFilter)
cv2.imshow("Original Bilateral",imgBilateral)

## Blur Image ##
cv2.imshow("Blur Image", blurImage)
cv2.imshow("Gaussan Image",gaussanBlurImage)
cv2.imshow("Median Blur",medainBlur)
cv2.imshow("Bilateral Blur",bilateralFun)

cv2.waitKey(0)
cv2.destroyAllWindows()