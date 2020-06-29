import numpy as np
import cv2

## Fotoğrafları Okuyalım ##
img1 = cv2.imread("img/text.png")
img2 = cv2.imread("img/contour.png")

## Fotoğrafı Gri Renge Çevirelim ##
grayImg1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

## Corners Bulalım goodFeaturesToTrack 4 parametre alır
# 1. parametre Fotoğrafın Gri olduğu hali vermek gerekir. float32 tipinde olmalı
# 2. Maximum kaç köşe bulsun onu girelim
# 3. parametre kalite değeridir. Deneyseldir
# 4. parametre köşeler arası minimum uzaklık girilir. ##
grayImg1 = np.float32(grayImg1)
cornersImg1 = cv2.goodFeaturesToTrack(grayImg1,100,0.01,10)

## Köşeleri Çizmek İçin Dönüşüm Yapılmalı
#  Float sayılar kullanamayacağımız için int'e convert etmeliyiz ##
cornersImg1 = np.int0(cornersImg1)

## Ekrana Yazdırmak İçin ##
for i in cornersImg1:
    ## cornersImg1 içerisinde ki değerleri tek satıra indirger.
    xAxis,yAxis = i.ravel()
    cv2.circle(img1,(xAxis,yAxis),3,(0,0,255),-1)

cv2.imshow("Corner",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
