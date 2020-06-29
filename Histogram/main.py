## Histogram : Fotoğraflar üzerinde çözümleme yapmamızı sağlar. Bir grafik olarak düşünülür. Fotoğrafın değer
# yoğunluklarını bize verir. Karanlık, Aydınlık Noktaları, Konstrat bilgilerine ulaşmamızı sağlayabilir. ##

from matplotlib import pyplot as plt
import numpy as np
import cv2

## Bir Siyah Ekran Oluşturalım
# 500x500'lik 0'lar bize siyah bir ekran verir.
# +50 yazarsak 0'lar 50 olur ve 50'lilerden oluşan bir matris oluşmuş olur ##
blackboard = np.zeros((500,500),np.uint8) + 50

## Fotoğraf okuduk ##
img = cv2.imread("img/median.png")

## B - G - R Renklerine ulaşalım ##
b,g,r = cv2.split(img)

## Histogramda Gösterelim ##
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

## Rectangle çizelim ##
cv2.rectangle(blackboard,(0,60),(200,150),(255,255,255),-1)


## Siyah Ekranımızı Gösterelim ##
#cv2.imshow("Blackboard",blackboard)

## Histogramı oluşturalım ##
#plt.hist(blackboard.ravel(),256,[0,256])

## Histogramı Ekranda Gösterelim ##
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()