## Image Save : Bir fotoğraf üzerinde değişiklik yaptıktan sonra, o fotoğrafı kaydetmek istediğimizde cv2.imwrite() metodu kullanılır.

## cv2.imwrite fonksiyonunun 2 parametresi vardır.
## 1.parametre hangi isimde kayıt edileceğini bize gösterir.
## 2.parametre kaydedilecek olan fotoğrafın değişkenidir.

import numpy as np
import cv2

print("------ cv2.imwrite() fonksiyonu ile okuduğumuz fotoğrafı kayıt edelim -----")
img = cv2.imread("img/bart.png",cv2.IMREAD_GRAYSCALE)  ## Fotoğrafı Gri'ye çevirerek okudum ve değişkene atadım
cv2.imwrite("bartgray.png",img)                        ## bartgray.png fotoğrafı çalışma dizinine geldi.

## Example: s tuşuna bastığımızda fotoğraf savePhoto klasörü içerisine dışarıdan okunan fotoğraf kayıt edilsin ##
img1 = cv2.imread("img/bart.png")   ## Fotoğrafı okuduk
cv2.imshow("Image", img1)           ## Kayıt Edilecek Fotoğrafı Ekranda Gösterdim
key  = cv2.waitKey(0)               ## Klavyeden Tıklanacak Olan Tuşu Aldım

if(key == 27):
    cv2.destroyAllWindows() ## Klavyede ESC tuşu 27'dir. Eğer ESC tuşuna basılırsa kayıt yapma ve ekranda gösterilen fotoğrafı kaldır.
elif(key == ord('s')):
    ## Klavyeden s tuşuna basılırsa, fotoğrafı savePhoto klasörü içerisine newPhoto.png olarak kaydet ve ekranda gösterilen fotoğrafı kaldır.
    cv2.imwrite("savePhoto/newPhoto.png",img1)
    cv2.destroyAllWindows()