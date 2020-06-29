## Image Okuma : işlenecek olan fotoğrafın dışarıdan alınması işlemidir. Aynı input ile dışarıdan bir sayı alıp o sayıy nasıl bir değişkene atıyorsak, burada da fotoğrafı
## dışarıdan alıp, o fotoğrafı bir sayı dizisine çevirip değişkene atayalım.

import numpy as np  ## numpy kütüphanesini ekledik
import cv2          ## cv2 kütüphanesini ekledik (openCV)

## Fotoğrafı Okuyalım cv2.imread() fonksiyonu ile okuma işlemi yapılır Fotoğraf yolunu(path'ini) fonksiyona verelim ##

## --------------------------------- cv2.imread() Fonksiyonu hakkında start --------------------------------- ##
## cv2.imread() fonksiyonu 2 parametre alır. 1 parametre fotoğrafın path'i
## 2.parametre ise flag'tir. Görüntünün nasıl okunacağını bize gösterir.
## * cv2.IMREAD_COLOR : Varsayılandır. Görüntü renkli bir şekilde okunur, saydamlık olmaz
## * cv2.IMREAD_GRAYSCALE : Görüntüyü gri şekilde yükler
## * cv2.IMREAD_UNCHANGED : Görüntüyü alpha kanalı ile yükler, saydamlık belirtir.
## --------------------------------- cv2.imread() Fonksiyonu hakkında end --------------------------------- ##

print("----- cv2.imread() ile fotoğraf okuyalım ----- ")
img1 = cv2.imread("img/bart.png")                       ## 2.parametre boş bırakıldığı zaman cv2.IMREAD_COLOR default olarak eklenir.
img2 = cv2.imread("img/bart.png",cv2.IMREAD_GRAYSCALE)  ## 2.parametre cv2.IMREAD_GRAYSCALE seçildi, görüntü gri olarak gösterilir.
img3 = cv2.imread("img/bart.png",cv2.IMREAD_UNCHANGED)  ## 2.parametre cv2.IMREAD_UNCHANGED seçildi, görüntü alpha channel ile gösterilir.

## Fotoğrafı Gösterelim cv2.imshow() fonksiyonu ile fotoğrafı ekranda gösterelim print() fonksiyonu nasıl ekranda sayı gösterirse imshow() fonksiyonu da fotoğraf gösterir. ##

## --------------------------------- cv2.imshow() Fonksiyonu hakkında start --------------------------------- ##
## cv2.imshow() fonksiyonu 2 parametre alır.
## 1.parametre fotoğraf imshow ile bir ekranda gösterilir. O ekranın başlığı ne olacaksa string olarak verilir.
## 2.parametre ise imread ile okuduğumuz fotoğrafı hangi değişkene atadıysak o değişkeni 2.parametre olarak vermemiz gerekir.
## --------------------------------- cv2.imshow() Fonksiyonu hakkında end ----------------------------------- ##
print("----- cv2.imshow() ile fotoğrafı gösterelim -----")
cv2.imshow("cv2.IMREAD_COLOR Olarak Okunan Fotoğraf",img1)
cv2.imshow("cv2.IMREAD_GRAYSCALE Olarak Okunan Fotoğraf",img2)
cv2.imshow("cv2.IMREAD_UNCHANGED Olarak Okunan Fotoğraf",img3)

## cv2.waitkey(0) kodunu kullanmamız gerekir. waitkey() fonksiyonu klavyeden herhangi bir tuşa basılmasını bekler,
## eğer biz bu komutu kullanmazsak fotoğraflar ekranda durmaz, hemen kapanır. Çünkü fotoğraflar imshow() ile gösterilir,
## ve hemen ekrandan kaldırılır

cv2.waitKey(0)

## cv2.destroyAllWindows() ise tüm ekranları arka planda kapatarak bellek harcamamızı en aza indirir.
cv2.destroyAllWindows()
