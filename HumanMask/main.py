import numpy as np
import cv2

## Trackbar Kullanmak İçin Etkisiz Bir Function oluşturalım, hata almayalım diye ##
def dummyFunction(x):
    pass

## PC Webcaminden Veri Alalım ##
## VideoCapture(0) diyerek, WebCam Açılır ##
cameraNumber = 0
video = cv2.VideoCapture(cameraNumber + cv2.CAP_DSHOW)

## Trackbar için window(pencere) oluşturalım ##
## Trackbar adından bir pencere oluşturdum   ##
cv2.namedWindow("Trackbar")

## Trackbar Penceresi Ekranı Tamamen Kaplamaması İçin Resize(Yeniden Boyutlandırma) yapalım ##
## Trackbar isimli pencereyi 500x500 boyutunda bir pencere oluşturalım                      ##
cv2.resizeWindow("Trackbar",500,500)

## Trackbar Üzerinde ki Switch(Anahtarları İleri Geri Yapılan)leri Oluşturalım ##
## 1. parametre Switch'in Adı
#  2. parametre Hangi ekranın üzerinde olacak, Trackbar isimli window'un üzerinde olacak dedim
#  3. ve 4. parametre lower ve upper değer en düşük 0 en yüksek 180 olacak dedim
#  5. parametre hata almamak için yazdığım gereksiz olan fonksiyon ##
cv2.createTrackbar("LOWER-H","Trackbar",0,180,dummyFunction) ## H 0-180 Arasundadır.
cv2.createTrackbar("LOWER-S","Trackbar",0,255,dummyFunction) ## S 0-255 Arasundadır.
cv2.createTrackbar("LOWER-V","Trackbar",0,255,dummyFunction) ## V 0-255 Arasundadır.

cv2.createTrackbar("UPPER-H","Trackbar",0,180,dummyFunction) ## H 0-180 Arasundadır.
cv2.createTrackbar("UPPER-S","Trackbar",0,180,dummyFunction) ## S 0-255 Arasundadır.
cv2.createTrackbar("UPPER-V","Trackbar",0,180,dummyFunction) ## V 0-255 Arasundadır.

## Oluşturulan Switch'ler hangi değer aralıklarında dursun. UPPER olanların değeri en sonda 255'te, LOWER olanlar ise 0'da yani en başta olsun ##
cv2.setTrackbarPos("UPPER-H","Trackbar",180) ## UPPER-H isimli Switch Trackbar Window'u üzerinde 180 değerinde olacak şekilde ayarlansın dedim
cv2.setTrackbarPos("UPPER-S","Trackbar",255) ## UPPER-S" isimli Switch Trackbar Window'u üzerinde 255 değerinde olacak şekilde ayarlansın dedim
cv2.setTrackbarPos("UPPER-V","Trackbar",255) ## UPPER-V isimli Switch Trackbar Window'u üzerinde 255 değerinde olacak şekilde ayarlansın dedim

## Video Çektiğimiz İçin While Döngüsü ile Frame'lere Ulaşmak Zorundayım ##
while(video.isOpened()):
    booleanValues, Frames = video.read()

    ## Bilgisayar WebCam'den okuma işlemi yapacağım için görüntü ters olur. Aynı telefonda ön kameradan fotoğraf çektikten sonra görüntünün kendiliğiden
    #  ters çevrilmesi bu yüzdendir. cv2.flip() fonksiyonu ile gelen Frame'lerin düz gözükmesi (1 değeri ile 2.parametre) sağlanır##
    Frames = cv2.flip(Frames,1)

    hsvFormatImage = cv2.cvtColor(Frames, cv2.COLOR_BGR2HSV)  ## Mask yapacağım için her frame'i HSV'ye dönüştürdüm

    ## Trackbar kullanmasaydım, hangi rengi maskelemek istiyorsam onun renklerinin upper ve lower değerlerini tanımlamam gerekiyordu
    # Şimdi ben o upper ve lower değerlerini trackbar'dan alacağım çünkü öyle planladık trackbar'dan o değerleri okuyalım ve değişkenlere atalım ##

    LowerHValue = cv2.getTrackbarPos("LOWER-H","Trackbar")  ## Trackbar Window'u üzerinde bulunan LOWER-H isimli Switch'ten gelen değeri LowerHValue değişkenine atadım
    LowerSValue = cv2.getTrackbarPos("LOWER-S","Tracbar")  ## Trackbar Window'u üzerinde bulunan LOWER-S isimli Switch'ten gelen değeri LowerSValue değişkenine atadım
    LowerVValue = cv2.getTrackbarPos("LOWER-V","Tracbar")  ## Trackbar Window'u üzerinde bulunan LOWER-V isimli Switch'ten gelen değeri LowerVValue değişkenine atadım

    UpperHValue = cv2.getTrackbarPos("UPPER-H","Trackbar")  ## Trackbar Window'u üzerinde bulunan UPPER-H isimli Switch'ten gelen değeri UpperHValue değişkenine atadım
    UpperSValue = cv2.getTrackbarPos("UPPER-S","Trackbar")  ## Trackbar Window'u üzerinde bulunan UPPER-S isimli Switch'ten gelen değeri UpperSValue değişkenine atadım
    UpperVValue = cv2.getTrackbarPos("UPPER-V","Trackbar")  ## Trackbar Window'u üzerinde bulunan UPPER-V isimli Switch'ten gelen değeri UpperVValue değişkenine atadım

    ## Aldığımız değerlerden upper ve lower olmak üzere bir array oluşturalım ##
    upperValues = np.array([UpperHValue, UpperSValue, UpperVValue])
    lowerValues = np.array([LowerHValue, LowerSValue, LowerVValue])

    ## Maskelenmiş Fotoğrafları maskedImage değişkenine atayalım ##
    maskedImage = cv2.inRange(hsvFormatImage, lowerValues, upperValues)

    ## Ekranda Gösterelim ##
    cv2.imshow("Masked Image Live", maskedImage)

    if(cv2.waitKey(5) & 0xFF == ord('q')):
        break
video.release()