print("""---------------------------------------
           HESAPLAMA ARACI
        (çıkmak için q'ya basın)
---------------------------------------""")

durum=" "
eskenar = "ve bu şekil bir eşkenar üçgendir."
ikizkenar = "ve bu şekil bir ikizkenar üçgendir"
diger = "ve bu şekil sıradan bir üçgendir"

def ucgen(a,b,c):
    global durum
    if(a == b and a == c):
        durum = eskenar
    if(a == b or b == c or a == c):
        durum = ikizkenar
    else:
        durum = diger
    return durum
  
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

        ucgen(bir,iki,uc)

        if(abs(iki-uc) < bir < iki + uc):
            print("Kenarlarını girdiğiniz şekil üçgen belirtmektedir",durum)
            break
        if(abs(bir-uc) < iki < bir + uc):
            print("Kenarlarını girdiğiniz şekil üçgen belirtmektedir",durum)
            break
        if(abs(bir-iki) < uc < bir + iki):
            print("Kenarlarını girdiğiniz şekil üçgen belirtmektedir",durum)
            break
        else:
            print("Kenarlarını girdiğiniz şekil üçgen belirtmemektedir, tekrar deneyin")
  
    if(soru == "q"):
        break
 
    else:
        print("Lütfen geçerli bir işlem girin..")