"""
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve 
soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

    isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

    soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
"""
import time


isim_list = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim_list = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]


tam_isim = list(zip(isim_list,soyisim_list))

for k,l in tam_isim:
    print(k,l)

print("\n\nisminiz listede yoksa eklemek zorundasınız: \n")


while True:
    soru = input("\nİsminiz listede var mı? (y/n): ")

    if(soru == "y" or soru == "Y"):
        time.sleep(0.3)
        print("\nSorun yok gibi gözüküyor..")
        time.sleep(0.8)
        break

    elif(soru == "n" or soru == "n"):
        ad = input("\nAdınız: ")
        soyad = input("soyadınız: ")
        
        isim_list.append(ad)
        soyisim_list.append(soyad)

        tam_isim = list(zip(isim_list,soyisim_list))

        for m,n in tam_isim:
            print("\n",m,n)

