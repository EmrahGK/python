import os as pc
import time

pc.system('cmd /c "color b"')

print("""
-----------------------------------

    Bilgisayar kapatma/yeniden
        başlatma programı

    (çıkmak için q'ya basın.)

        İşlemler:
            1.Kapatma
            2.Yeniden başlatma

-----------------------------------
""")

def kapat():
    pc.system("shutdown /s /t 1")
    time.sleep(0.5)
    print("Görüşürüz sahip..")

def yenidenbaslat():
    pc.system("shutdown /r /t 1")
    time.sleep(0.5)
    print(".")

while True:
        
    islem = str(input("\n\nİşlemi girin(1-2): "))
    
    if(islem == "q"):
        print("\nProgramdan çıkılıyor..")
        time.sleep(1.5)
        break

    elif(islem == "1"):

        soru = str(input("\nBilgisayarınızı kapatmak istiyorsunuz. Emin misiniz(y/n): "))
        if(soru == "y" or soru == "Y"):
            print("\nBilgisayar kapatılıyor..")
            #kapat fonksiyonunu çağırıcağız (ileride)
            kapat()
            time.sleep(2)
            break
        elif(soru == "n" or soru =="N"):
            print("\n(Ana menüye yönlendiriliyorsunuz..)")
            time.sleep(1)
            continue
        else:
            print("Lütfen geçerli bir işlem girin..")
            time.sleep(1)
            continue

    elif(islem == "2"):

        soru = str(input("Bilgisayarınızı yeniden başlatmak istiyorsunuz. Emin misiniz?(y/n): "))
        if(soru == "y" or soru == "Y"):
            print("\nBilgisayar yeniden başlatılıyor..")
            #yeniden başlat fonksiyonunu ekleyeceğiz (ileride..)
            yenidenbaslat()
            time.sleep(2)
            break
        elif(soru == "n" or soru =="N"):
            print("Ana menüye yönlendiriliyorsunuz..")
            time.sleep(1)
            continue
        else:
            print("Lütfen geçerli bir işlem girin..")
            time.sleep(1)
            continue

    else:
        print("Hatalı bir işlem girdiniz. Tekrar deneyin..")
        time.sleep(0.5)

