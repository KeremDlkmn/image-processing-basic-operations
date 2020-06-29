import numpy as np
import cv2

## Fotoğrafı Okuyalım ##
## img klasörü içerisinde ki fotoğrafı okudum ve img değişkenine atadım
img = cv2.imread("img/bart.png")

## Her fotoğraf piksellerden oluşur. Bu pikseller R-G-B renk komutları ile çalışırlar. Her piksel 0 - 255 bit yani 256 bitten oluşur. ##

pixel = img[100,100] ## X ekseninde 100.nokta ile Y ekseninde 100.noktada ki o piksel'i aldık ve pixel adlı değişkene atadık ##
print(pixel)         ## [0 116 141] sonucunu elde ettik. Bu sonuç B - G - R renklerinin değerleridir. Yukarıda yazdığım gibi 0 ile 255 arasında değer alırlar.

## Blue, Green, Red pixellerini bulalım ##
bluePixel  = img[100,100,0]  ## 100'e 100 noktasında ki 0(Blue) pikselinin değerini versin  ##
greenPixel = img[100,100,1]  ## 100'e 100 noktasında ki 1(Green) pikselinin değerini versin ##
redPixel   = img[100,100,2]  ## 100'e 100 noktasında ki 2(Red) pikselinin değerini versin   ##

print("Blue  Pixel Value : ", bluePixel)
print("Green Pixel Value : ", greenPixel)
print("Red   Pixel Value : ", redPixel)

## Herhangi bir pixel'deki rengi değiştirelim ##
newPixel = img[150,170] = [0,0,0] ## 100'e 100 noktasında ki pixelleri B - G -R piksellerini beyaz yaptık

## 150'ye 170 olan piksel noktasının rengi artık 0 0 0 oldu
print(newPixel)