import numpy as np
import cv2

## Fotoğrafı Okuyalım GRAYSCALE olarak okuduk ##
img = cv2.imread("img/bart.png",0)

## image shape bize fotoğrafın kaç satır ve sütundan(piksel sayıları) oluştuğunu bize söyler ##
row, column = img.shape

## Matrix'i Oluşturalım [1,0,10]'X ekseninde 10 piksel(soldan sağa),  [0,1,70]'Y ekseninde 70 piksel seçildi(yukarıdan aşağıya) ##
Matrix = np.float32([[1,0,0],[0,1,70]])

## Belirlediğim değerleri(Transformasyon Matrix) uygulayalım 1. parametre fotoğrafın kendisi, 2. parametre matrix
#  3.parametre fotoğrafımın satır ve sütun sayısıdır. ##
dst = cv2.warpAffine(img,Matrix,(row,column))

## Yeni fotoğrafı gösterelim ##
cv2.imshow("IMAGE",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()