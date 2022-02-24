

alfabe = "abcçdefhğhıijklmnoöpqrsştuüvwxyz0"

while(True):
    
    metin = input("\nmetni girin: ")

    try:
        metin = str(metin)
        metin.lower()
        metin.replace(" ","")
    except:
        print("Beklenmeyen bir hata meydana geldi. Tekrar deneyin..")
        continue
    
    if(metin == "q"):
        print("programdan çıkılıyor.")
        break

    for i in alfabe:
        sayi = metin.count(i)

        if(sayi == 0):
            print(f"{i} harfi cümlede yoktur")
        else:
            print(f"{i} harfi cümlede {sayi} tanedir")
        if(sayi == "0"):
            break












