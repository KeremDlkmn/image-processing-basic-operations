import numpy as np
import cv2

## Fotoğrafı Okuduk ##
img1 = cv2.imread("img/bart.png")
img2 = cv2.imread("img/lisa.png")

print(img1.shape)
print(img2.shape)
img3 = img2[0:274,0:184]    ## Fotoğrafları üst üste eklemek için aynı boyutta olması gerekiyor. img2'yi img1 ile aynı boy yaptık (274x184)

## Fotoğrafları Ekleyelim ##

## addWeighted() fonksiyonu 5 paramtre alır.
## 1. parametre eklenecek olan ilk fotoğraf
## 2. parametre 1.fotoğrafı hangi yoğunlukta(alpha yani opacity değeri) eklemek istiyorum en fazla 1 değeri alabilir.
## 3. parametre eklenecek olan 2.fotoğraftır.
## 4. parametre 2.fotoğraf hangi yoğunlukta eklenecek. Ama bu 2.parametreye bağlıdır. Ben ikinci parametreye 0.8 dedim toplamda 1.0 olmalı o zaman buraya 0.2 değeri kalır.
## 5. parametre beta olarak geçer. 0 ya da 1 değeri alır. Denklemi sağlamak için verilen bir parametredir.
newImg = cv2.addWeighted(img1,0.8,img3,0.2,1)

cv2.imshow("Image",newImg)

cv2.waitKey(0)
cv2.destroyAllWindows()