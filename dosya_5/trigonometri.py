#Trigonometri hesapalama aracı (Bunu yapmam biraz zor olacak çünkü trigonometre bilmiyorum sayılır xd)


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
    
    print("\n(Çıkmak için q'ya basın)\n")
    islem = str(input("İşlemi girin(1-4): "))

    if(islem == "q"):
        print("\n\nProgramdan çıkılıyor..\n")
        break

    hipotenus = int(input("\nHipotenüs'ü girin: "))
    karsi = int(input("Karşı kenarı girin: "))
    komsu = int(input("Komşu kenarı girin: "))

    #önemli not: yarın if durumlarını ayarlayacağım. hata vermemesi için şimdilik sadece işlemi yazdırıyorlar. (27.01.2022)

    if(islem == "1"):
        #Kosinüs işlemi
        print("İşlem Kosinüs\n")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Kosinüs(α) = ",kosinus(hipotenus,karsi,komsu))

    elif(islem == "2"):
        #Sinüs işlem
        print("İşlem Sinüs\n")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Sinüs(α) = ",sinus(hipotenus,karsi,komsu))

    elif(islem == "3"):
        #3.Tanjant işlemi
        print("İşlem Tanjant\n")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Tanjant(α) = ",tanjant(hipotenus,karsi,komsu))
        
    elif(islem == "4"):
        #4.Kotanjant işlemi
        print("İşlem Kotanjant\n")
        if(hipotenus == "q" or karsi == "q" or komsu == "q"):
            break
        print("Kotanjant(α) = ",kotanjant(hipotenus,karsi,komsu))


    else:
        print("\nLütfen geçerli bir işlem giriniz..")


