## Contours: Bir nesnenin, bir fotoğrafın sınır çizgileridir.
#  Arda arada gelmiş noktalardan oluşur. ##
import cv2

## Fotoğrafı Okuduk ##
image = cv2.imread("img/contours.png")

## Fotoğrafı Gri'ye Çevirelim ##
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

## Trashold İşlemi Yapalım ##
_,thresh = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)

## contours fonksiyonu 2 değer döndürür
#  1.değer gereksiz değer
#  2. değer contours bizim için gereklidir.##

## contours fonksiyonun parametreleri
#  1.parametre threshli fotoğraftır.
#  2. ve 3. parametre daha da iyi sonuç vermesini sağlar
#  bu fonksiyon sayesinde fotoğrafın kenarlarının koordinatları bulunmuş olur. ##
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

## Koordinatları çizelim
#  1. parametre hangi fotoğrafın üzerinde çizeceğim?
#  2. parametre koordinatlar
#  3. parametre -1
#  4. parametre renkler
#  5. parametre kalınlık##
cv2.drawContours(image,contours,-1,(0,0,255),3)

## Gösterelim ##
cv2.imshow("contour",image)
cv2.waitKey(0)
cv2.destroyAllWindows()