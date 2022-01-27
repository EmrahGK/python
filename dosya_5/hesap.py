#Trigonometri hesapalama aracı (Bunu yapmam biraz zor olacak çünkü trigonometre bilmiyorum xd)

#bu kodu hazır math modülü sayesinde biraz daha koddan tasarruf edebildiğimizi göstermek için yazdım. Diğer dosyada kısa olan
#kullanım var.

print("""
--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-

                _/﹋\_
                (҂`_')
                <,︻╦╤─ ҉* _ _ 
                _/﹋\_

        Trigonometri hesaplama aracı
          (çıkmak için q'ya basın.)

        İşlemler:
            1.Kosinüs
            2.Sinüs
            3.Tanjant
            4.Kotanjant


                      /|
                     / |
                    /  |
                   /   |
                  /    |   
     HİPOTENÜS   /     | KARŞI
                /      |
               /       |
              /        |
             /         |
            /\'α'       |
            ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
               KOMŞU

--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-
""")

global a,b,c

def kosinus(a,b,c):
    return c / a

def sinus(a,b,c):
    return b / a

def tanjant(a,b,c):
    return b / c

def kotanjant(a,b,c):
    return c / b  
        
while True:

    islem = str(input("İşlemi girin(1-4): "))

    hipotenus = int(input("Hipotenüs'ü girin: "))
    karsi = int(input("Karşı kenarı girin: "))
    komsu = int(input("Komşu kenarı girin: "))

    #önemli not: yarın if durumlarını ayarlayacağım. hata vermemesi için şimdilik sadece işlemi yazdırıyorlar. (27.01.2022)

    if(islem == "1"):
        #Kosinüs işlemi
        print("İşlem Kosinüs(yanlış girdiyseniz q'ya basın)")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Kosinüs(α) = ",kosinus(hipotenus,karsi,komsu))

    elif(islem == "2"):
        #Sinüs işlem
        print("İşlem Sinüs(yanlış girdiyseniz q'ya basın)")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Sinüs(α) = ",sinus(hipotenus,karsi,komsu))

    elif(islem == "3"):
        #3.Tanjant işlemi
        print("İşlem Tanjant(yanlış girdiyseniz q'ya basın)")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Tanjant(α) = ",tanjant(hipotenus,karsi,komsu))
        
    elif(islem == "4"):
        #4.Kotanjant işlemi
        print("İşlem Kotanjant5(yanlış girdiyseniz q'ya basın)")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Kotanjant(α) = ",kotanjant(hipotenus,karsi,komsu))

    elif(islem == "q"):
        print("Programdan çıkılıyor..")
        break

    else:
        print("Lütfen geçerli bir işlem giriniz..")


