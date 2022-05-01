# bu programın amacı matematiksel olasılığın deneysel olasılıkla olan ilişkisini test etmek için programlandı (fikri bana ait) 
# şimdilik yazı tura işlemini yapacağım ileride 1-100 arası sayılarla olan versionu da gelebilir.


import random
import time

liste = ["tura","yazı"]


yazı_list = []
tura_list = []
sınır = range(1000000)

def flipcoin(a):
    return random.choice(a)

for i in sınır:
    if i == 999999:
        sayı_y = len(yazı_list)
        sayı_t = len(tura_list)
        print("Döngü sonlandı..")
        toplam = sayı_t + sayı_y

        oran_y = sayı_y / toplam
        oran_t = sayı_t / toplam

        print("Yazı gelme oranı: %",oran_y)
        print("Tura gelme oranı: %",oran_t)

        break
    else:
        randomed = flipcoin(liste)
        if(randomed == "tura"):
            tura_list.append("tura")
        elif(randomed == "yazı"):
            yazı_list.append("yazı")






        




















