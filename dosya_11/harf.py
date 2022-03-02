import time 
import sys

alfabe = "abcçdefhğhıijklmnoöpqrsştuüvwxyz0"

def yazdir(yazi):
    for letter in yazi:
        time.sleep(0.02) 
        sys.stdout.write(letter)
        sys.stdout.flush()

while(True):
    time.sleep(1)
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
        time.sleep(1)
        sys.exit()

    for i in alfabe:
        
        if(i == "0"):
            break
        else:
            
            sayi = metin.count(i)
            if(sayi == 0):
                time.sleep(0.1)
                a = f"{i} harfi cümlede yoktur\n"
                yazdir(a)

            else:
                time.sleep(0.1)
                a = f"{i} harfi cümlede {sayi} tanedir\n"
                yazdir(a)

        






