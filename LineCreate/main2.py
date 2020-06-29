import numpy as np
import cv2

## 512,512,3 -> 512x512'lik ve RGB renk kodlarına sahip bir matris oluşturdum
## np.uint8 ile bu matisi integer(tam sayı)'a çevirdim
## Artık img değişkeni içerisinde 512x512 boyutunda siyah bir ekran oluşmuş oldu
img = np.zeros((512,512,3),np.uint8)

## cv2.line() fonksiyonunu kullanarak img üzerine bir çizgi çizeceğiz.
## 1.parametre 512x512'lik ekranım
## 2.parametre sol üst köşenin koordinatları
## 3.parametre sağ alt köşenin koordinatları
## 4.parametre renk kodudur. RGB renk koduna göre girilir değerler.
## 5.parametre çizginin kalınlığı
cv2.rectangle(img,(0,0),(100,100),(255,255,255),5)

cv2.imshow("Background",img)

cv2.waitKey(0)
cv2.destroyAllWindows()