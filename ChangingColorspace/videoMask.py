import numpy as np
import cv2

## HSV Renk Formatı: Bir videodaki Frame'leri BGR'dan HSV'ye çevirerek bazı renkleri yok etmek istediğimde bu dönüşümü yaparım ##
video = cv2.VideoCapture("video/original.avi")

while(video.isOpened()):
    booleanValues,frames = video.read()

    if(booleanValues): ## True Geldikçe
        hsvFormat = cv2.cvtColor(frames,cv2.COLOR_BGR2HSV)  ## Video'daki her Frame'i al BGR'dan HSV'ye çevirdik

        ## Video'da ortada bulunan sarı rengi kaldırmak istiyoruz. HSV'ye çevirdik evet ama orada ki Sarı rengi kaldırmak için taban ve üst sarı renkleri belirleyelim ##
        upperYellow = np.array([48,255,255])
        lowerYellow = np.array([18,94,150])

        ## O sarı rengi maskelememiz lazım ##
        ## inRange() fonksiyonu ile yaparız. 1.parametre hangi fotoğraf'a uygulayacağız, 2.parametre ve 3.parametre ise lower ve upper yellow değerleridir. ##
        mask = cv2.inRange(hsvFormat,lowerYellow,upperYellow)

        cv2.imshow("MASK",mask)                 ## Görüntü açıldığında yol ortasında bulunan sarı renk beyaz bir şekilde maskelenmiş halde gözekecetir.
    if(cv2.waitKey(20) & 0xFF == ord('q')):
        break
video.release()
cv2.destroyAllWindows()
