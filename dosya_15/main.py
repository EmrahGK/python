"""1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın."""

from logging.config import listen
from operator import truediv

sınır =  101
sayı_list = range(1,sınır)

for i in sayı_list:
    if i == 1:
        durum = False
    if i == 2:
        durum = True    
    else:
        liste = range(1,i)
        for j in liste:
            kalan = i % j
            asd = []
            for i in sınır():
                asd.append(i)
            if kalan == 0:
                asd[i] = True
            else:
                asd[i] = False
            hepsi = all(asd)
            if hepsi == True:
                print(f"{i} bir asal sayıdır.")
                
            elif hepsi == False:
                print(f"{i} bir asal sayı değildir.")
            else:
                print("HATAQAAAAA!!!")