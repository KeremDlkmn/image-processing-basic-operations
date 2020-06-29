import numpy as np
import cv2

## Fotoğrafı Okuyalım ##
img = cv2.imread("img/bart.png",0)

## Fotoğrafın Satır ve Sütun Değerlerini Alalım -> Eğer img GRAYSCALE(0) olarak okunmazsa BGR'da row,column,colorChannel
# olmak üzere 3 tane value döner ##
row, column = img.shape

## Bir Matrix Değeri Oluşturalım 2D'de rotasyon işlemini yazalım
#  1. parametre column -> column/2 yaparak bir ölçek belirledik istediğimiz değerleri yazabiliriz fakat düzgün gözükmesi gerekir.
#  2. parametre row    -> row içinde column'da anlatılan geçerlidir.
#  3. parametre kaç derece döneceği
#  NOT: Saat yönünün tersine döndürür ##

Matrix = cv2.getRotationMatrix2D((column/2,row/2),90,1)

## Bu matrix'i fotoğrafa uygulayalım ##
dst = cv2.warpAffine(img,Matrix,(column,row))

## Fotoğrafı Ekranda Gösterelim ##
cv2.imshow("IMAGE",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()