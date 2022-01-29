import os as pc
import time

pc.system('cmd /c "color b"')

print("""
_______________________________________________

   Şifreleyici ve Şifreyi Çözücü Program
        (çıkmak için q'ya basın)


            İşlemler:
                1.Şifrele
                2.Şifreyi çöz

        NOT: Kaç harli şifreleme
        yapıldığını bilmiyorsanız
        İlk soruyu 'Sezar' olarak
        yanıtlayın.

______________________________________________
""")

global metin

normal = "ABCÇDEFGĞHIIJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz0123456789!'^+%&/()=?_"

#tek harfli şifreleme kısmı
encrypted1 = "BCÇDEFGĞHIIJKLMNOÖPRSŞTUÜVYZAbcçdefgğhıijklmnoöprsştuüvyza1234567890'^+%&/()=?_!"
sifrele1 = str.maketrans(normal,encrypted1)
coz1 = str.maketrans(encrypted1,normal)

#iki harfli şifreleme kısmı
encrypted2 = "CÇDEFGĞHIIJKLMNOÖPRSŞTUÜVYZABcçdefgğhıijklmnoöprsştuüvyzab2345678901^+%&/()=?_!'"
sifrele2 = str.maketrans(normal,encrypted2)
coz2 = str.maketrans(encrypted2,normal)

#üç harfli şifreleme kısmı
encrypted3 = "ÇDEFGĞHIIJKLMNOÖPRSŞTUÜVYZABCçdefgğhıijklmnoöprsştuüvyzabc3456789012+%&/()=?_!'^" 
sifrele3 = str.maketrans(normal,encrypted3)
coz3 = str.maketrans(encrypted3,normal)

#şifreleme fonksiyonları
def sifrele_1():
    return metin.translate(sifrele1)
def sifrele_2():
    return metin.translate(sifrele2)
def sifrele_3():
    return metin.translate(sifrele3)

#şifreyi çözme fonksiyonları
def coz_1():
    return metin.translate(coz1)
def coz_2():
    return metin.translate(coz2)
def coz_3():
    return metin.translate(coz3)
       

while True:
    
    soru = str(input("\nKaç harfli şifreleme yapmak istiyorsunuz (1-3): "))
    if(soru == "1"):
        #tek harfli şifreleme
        soru2 = str(input("\nİşlemi girin(1-2): "))
        if(soru2 == "1"):
            metin = str(input("\n\nŞifrelenecek metni girin: "))
            time.sleep(0.5)
            print("\nTek harfli olarak şifrelenmiş metin: ",sifrele_1())
        elif(soru2 == "2"):
            metin = str(input("\n\nŞifresi çözülecek metni girin: "))
            time.sleep(0.5)
            print("\nTek harfli şifrenin çözülmüş hali: ",coz_1)
        elif(soru2 == "q"):
            print("\nAna menüye yönlendiriliyorsunuz..")
            time.sleep(0.5)
            continue
        else:
            print("\nGeçerli bir işlem girin(1-2). İşlem '{}' olamaz".format(soru2))
            continue
    elif(soru == "2"):
        #iki harfli şifreleme
        soru2 = str(input("\nİşlemi girin(1-2): "))
        if(soru2 == "1"):
            metin = str(input("\n\nŞifrelenecek metni girin: "))
            time.sleep(0.5)
            print("\nİki harfli olarak şifrelenmiş metin: ",sifrele_2())
        elif(soru2 == "2"):
            metin = str(input("\n\nŞifresi çözülecek metni girin: "))
            time.sleep(0.5)
            print("\nTek harfli şifrenin çözülmüş hali: ",coz_2)
        elif(soru2 == "q"):
            print("\nAna menüye yönlendiriliyorsunuz..")
            time.sleep(0.5)
            continue
        else:
            print("\nGeçerli bir işlem girin(1-2). İşlem '{}' olamaz".format(soru2))
            continue
    elif(soru == "3"):
        #üç harfli şifreleme
        soru2 = str(input("\nİşlemi girin(1-2): "))
        if(soru2 == "1"):
            metin = str(input("\n\nŞifrelenecek metni girin: "))
            time.sleep(0.5)
            print("\nİki harfli olarak şifrelenmiş metin: ",sifrele_3())
        elif(soru2 == "2"):
            metin = str(input("\n\nŞifresi çözülecek metni girin: "))
            time.sleep(0.5)
            print("\nTek harfli şifrenin çözülmüş hali: ",coz_3)
        elif(soru2 == "q"):
            print("\nAna menüye yönlendiriliyorsunuz..")
            time.sleep(0.5)
            continue
        else:
            print("\nGeçerli bir işlem girin(1-2). İşlem '{}' olamaz".format(soru2))
            continue
    elif(soru == "Sezar" or soru =="sezar" or soru == "Caezar" or soru == "caezar"):
        print("\nSezar fonksiyonu, kaç harfli şifreleme yapıldığını bilmediğiniz durumlar içindir. \n\n")

        metin = str(input("Şifresi bilinmeyen metni girin: "))

        print("\nBu üç metinden biri muhtemelen anlamlı olacaktır. \n")
        print("\n\nBirinci metin: ",coz_1())
        print("\nİkinci metin: ",coz_2())
        print("\nÜçüncü metin: ",coz_3())
        continue
    elif(soru == "q"):
        print("\nProgramdan çıkılıyor..")
        time.sleep(1)
        break
    else:
        print("\nSadece 1 ve 3 arasında şifreleme yapabilirsiniz. İşlem '{}' olamaz".format(soru))
    
        