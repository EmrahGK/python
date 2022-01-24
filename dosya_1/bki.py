#Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

#BKİ 18.5'un altındaysa -------> Zayıf

#BKİ 18.5 ile 25 arasındaysa ------> Normal

#BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

#BKİ 30'un üstündeyse -------------> Obez

boy = input("boyunuzu girin(cm): ")
kilo = input("kilonmuzu girin(kg): ")

boy = float(boy)
kilo = float(kilo)

index = float(kilo / boy * boy)

print('''
********************************

BOT KİLO ENDEKSİ HESAPLAMA ARACI

   (çıkmak için q'ya basın..)

********************************
''')

while True:
    
    if(index <= 18.5):
        print("boy kilo endeksine göre zayıf birisiniz..")
        break

    elif(18.5 < index <= 25):
        print("boy kilo endeksine göre kilonuz normal")
        break

    elif(25 < index <= 30):
        print("boy kilo endeksine göre fazla kilolu birisiniz.")
        break   

    elif(index > 30):
        print("hesaplanan boy kilo endeksine göre obezsiniz.")
        break

    elif(boy == "q" or kilo == "q"):
        print("programdan çıkılyor..")
        break

    else:
        print("lütfen geçerli bir rakam girin")
        break


