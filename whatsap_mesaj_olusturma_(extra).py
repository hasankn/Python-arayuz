#whatsaptan hazır mesaj atma kodu
#hasan kaan kartal
#calistirdiktan sonra whatsaba gidip enter tuşuna basınca otomatik olarak ekrana yazıyı yazar
import pyautogui as pg
import time
time.sleep(5)
class isimler:
    hasan_kaan="hasan kaan kartal "
class hayvan():
    kedi="kedinizin"
    kopek="kopeginizin"
class uygulamalar():

    karma1 = "karma asilarinin ilki "
    karma2 = "karma asilarinin ikincisi"
    kuduz  = "kuduz asiniz"

mesaj="merhaba sayin {}  bugun {} {} icin calisma saatlerimiz arasinda kartal veteriner klinigine gelmenizi rica ediyoruz.İyi gunler diliyoruz".format(isimler.hasan_kaan,hayvan.kedi,uygulamalar.karma1)
for i in range(1):
    pg.write(mesaj)
    pg.press("enter")
