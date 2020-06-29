import numpy as np
import cv2

## Fotoğrafı Okuduk ##
img = cv2.imread("img/bart.png")

## ROI: Region Of Image, Fotoğrafın belirli bir bölgesine ulaşmamızı sağlar. ##

## Fotoğrafın Kaç'a Kaç olduğunu öğrenelim ##
print(img.shape)    ## (274, 184, 3) çıktısını elde ettik. Yani 274x184'lük bir fotoğrafım var.

## Fotoğrafta ki Bart'ın gövdesinden yukarsını seçmeye çalışalım ## img[25:130,0:150] 25:130 yukarıdan aşağıya doğru, 0:150 soldan sağa doğru resimleri keser ## ##

head = img[25:130,0:150]
cv2.imshow("Head of Bart",head)

cv2.waitKey(0)
cv2.destroyAllWindows()
