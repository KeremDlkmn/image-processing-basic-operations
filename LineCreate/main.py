import numpy as np
import cv2

## 512,512,3 -> 512x512'lik ve RGB renk kodlarına sahip bir matris oluşturdum
## np.uint8 ile bu matisi integer(tam sayı)'a çevirdim
## Artık img değişkeni içerisinde 512x512 boyutunda siyah bir ekran oluşmuş oldu
img = np.zeros((512,512,3),np.uint8)

## cv2.line() fonksiyonunu kullanarak img üzerine bir çizgi çizeceğiz.
## 1.parametre 512x512'lik ekranım
## 2.parametre çizginin başlangıç noktası
## 3.parametre çizginin bitiş noktası
## 4.parametre renk kodudur. RGB renk koduna göre girilir değerler.
## 5.parametre çizginin kalınlığı
cv2.line(img,(0,0),(360,480),(255,255,255),5)

cv2.imshow("Background",img)

cv2.waitKey(0)
cv2.destroyAllWindows()