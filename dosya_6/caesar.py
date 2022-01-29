import os
import time

print("""
--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-
--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-

   Şifreleyici ve Şifreyi Çözücü Program
        (çıkmak için q'ya basın)


            İşlemler:
                1.Şifrele
                2.Şifreyi çöz

--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-
--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-

""")

global metin

normal = "abcçdefgğhıijklmnoöprsştuüvyz0123456789"

#tek harfli şifreleme kısmı
encrypted1 = "bcçdefgğhıijklmnoöprsştuüvyza1234567890"
sifrele1 = str.maketrans(normal,encrypted1)
coz1 = str.maketrans(encrypted1,normal)

#iki harfli şifreleme kısmı
encrypted2 = "cdecçdefgğhıijklmnoöprsştuüvyzab2345678901"
sifrele2 = str.maketrans(normal,encrypted2)
coz2 = str.maketrans(encrypted2,normal)

#üç harfli şifreleme kısmı
encrypted3 = "decçdefgğhıijklmnoöprsştuüvyzabc3456789012" 
sifrele3 = str.maketrans(normal,encrypted3)
coz3 = str.maketrans(encrypted3,normal)

#şifreleme fonksiyonları
def sifrele_1():
    metin.translate(sifrele1)
def sifrele_2():
    metin.translate(sifrele2)
def sifrele_3():
    metin.translate(sifrele3)

#şifreyi çözme fonksiyonları
def coz_1():
    metin.translate(coz1)
def coz_2():
    metin.translate(coz2)
def coz_3():
    metin.translate(coz3)
    

while True:
    
    soru = str(input("Kaç harfli şifreleme yapmak istiyorsunuz (1-3): "))

    if(soru == "1"):
        #tek harfli şifreleme
        soru2 = str(input("İşlemi girin(1-2): "))
        if(soru2 == "1"):
            metin = str(input("Şifrelenecek metni girin: "))
            time.sleep(0.5)
            print("Tek harfli olarak şifrelenmiş metin: ",sifrele_1())
        elif(soru2 == "2"):
            metin = str(input("Şifresi çözülecek metni girin: "))
            time.sleep(0.5)
            print("Tek harfli şifrenin çözülmüş hali: ",coz_1)
        else:
            print("Geçerli bir işlem girin(1-2)..")
            zort = 5

        if(zort == 5):
            continue

    elif(soru == "2"):
        #iki harfli şifreleme
        soru2 = str(input("İşlemi girin(1-2): "))
        if(soru2 == "1"):
            metin = str(input("Şifrelenecek metni girin: "))
            time.sleep(0.5)
            print("İki harfli olarak şifrelenmiş metin: ",sifrele_2())
        elif(soru2 == "2"):
            metin = str(input("Şifresi çözülecek metni girin: "))
            time.sleep(0.5)
            print("Tek harfli şifrenin çözülmüş hali: ",coz_2)

    elif(soru == "3"):
        #üç harfli şifreleme
        soru2 = str(input("İşlemi girin(1-2): "))
        if(soru2 == "1"):
            metin = str(input("Şifrelenecek metni girin: "))
            time.sleep(0.5)
            print("İki harfli olarak şifrelenmiş metin: ",sifrele_3())
        elif(soru2 == "2"):
            metin = str(input("Şifresi çözülecek metni girin: "))
            time.sleep(0.5)
            print("Tek harfli şifrenin çözülmüş hali: ",coz_3)        
        


        