"""
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir 
satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

    coskun.m.murat@gmail.com
    example@xyz.com
    mustafa.com
    mustafa@gmail
    kerim@yahoo.com
"""
from re import search


white_mail_list = ("@gmail.com","@hotmail.com","@yahoo.com","@outlook.com","@icloud.com","@mac.com","@gmx.com","@yandex.com")

with open("mail.txt","r",encoding="utf-8") as file:

    file = file.read().split('\n')

    for i in file:
        
        for a in white_mail_list:
            
            sonuc = search(a,i)

            if(sonuc == None):
                pass
            else:
                print(i)
            

    





