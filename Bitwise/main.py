import numpy as np
import cv2

## Fotoğrafları Okuyalım ##
img1 = cv2.imread("img/bitwise1.png")
img2 = cv2.imread("img/bitwise2.png")

## bitwise and işlemi uygulayacağız
# img1 ve img2'yi and işlemine sokacağız ##
bitwiseAnd = cv2.bitwise_and(img2,img1)
bitwiseOr  = cv2.bitwise_or(img2,img1)
bitwiseXor = cv2.bitwise_xor(img2,img1)

## Fotoğrafı Gösterelim ##
cv2.imshow("ORIGINAL IMG1",img1)
cv2.imshow("ORIGINAL IMG2",img2)
cv2.imshow("AND",bitwiseAnd)
cv2.imshow("OR",bitwiseOr)
cv2.imshow("XOR",bitwiseXor)

cv2.waitKey(0)
cv2.destroyAllWindows()
