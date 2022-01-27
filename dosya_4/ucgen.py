#Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

#Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

#Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

#Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

#Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

#EmrahGK

print("""---------------------------------------
           HESAPLAMA ARACI
        (çıkmak için q'ya basın)
---------------------------------------""")

while True:
        
    soru = str(input("üçgen mi dörtgen mi?: "))


    if(soru == "dörtgen" or soru == "Dörtgen"):

        bir = int(input("Birinci kenarı gir: "))
        iki = int(input("İkinci kenarı gir: "))
        uc =  int(input("Üçüncü kenarı gir: "))
        dort = int(input("Dördüncü kenarı gir: "))


        if(bir == iki and bir == uc and bir == dort):
            print("Girdiğiniz şekil bir karedir..")
            break
        if(bir == uc and iki == dort):
            print("Girdiğiniz şekil bir dikdörtgendir..")
            break
        else:
            print("Girdiğiniz şekil sıradan bir dörtgendir..")
            break

    if(soru == "Üçgen" or soru == "üçgen"):
        
        bir = int(input("Birinci kenarı gir: "))
        iki = int(input("İkinci kenarı gir: "))
        uc =  int(input("Üçüncü kenarı gir: "))

        def ucgen(bir,iki,uc):
            if(bir == iki and bir == uc):
                print("bu şekil bir eşkenar üçgendir.")
            if(bir == iki or iki == uc or bir == uc):
                print("bu şekil bir ikizkenar üçgendir")
            else:
                print("bu şekil sıradan bir üçgendir")
        
        if(abs(iki-uc) < bir < iki + uc):
            print("Kenarlarını girdiğiniz şekil üçgen belirtmektedir ve")
            break
        if(abs(bir-uc) < iki < bir + uc):
            print("Kenarlarını girdiğiniz şekil üçgen belirtmektedir ve")
            break
        if(abs(bir-iki) < uc < bir + iki):
            print("Kenarlarını girdiğiniz şekil üçgen belirtmektedir ve",ucgen(bir,iki,uc))
            break
        else:
            print("Kenarlarını girdiğiniz şekil üçgen belirtmemektedir, tekrar deneyin")
        
    if(soru == "q"):
        break
    
    else:
        print("Lütfen geçerli bir işlem girin..")





