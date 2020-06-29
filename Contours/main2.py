## Image Moments: Bir nesnenin özelliklerinin tespit edilmesi sağlanır.
# Image Feature Extraction denebilir. ##
import cv2

## Fotoğrafı Okuyalım ##
image = cv2.imread("img/contours2.png")

## Fotoğrafı Gri'ye Çevirelim ##
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

## Thresh işlemi yapalım. ##
_,thresh = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)

## Image hakkında bize bilgiler verir. Bu bilgiler bir sözlük içerisind gelir.##
imageInfo = cv2.moments(thresh)

## Fotoğrafımızın Ağırlık Merkezini(Geometri Merkezi) Bulalım ##
X = int(imageInfo["m10"]/imageInfo["m00"])
Y = int(imageInfo["m01"]/imageInfo["m00"])

## Geometri Merkezini bir yuvarlak çizerek gösterelim ##
cv2.circle(image,(X,Y),5,(0,255,0),-1)

## Fotoğrafımızı Görelim ##
cv2.imshow("IMG",image)

cv2.waitKey(0)
cv2.destroyAllWindows()


