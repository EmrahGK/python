""" 
bu şekilde bir dosya oluşturun ve içinde şu satırlar yer alsın.

                    'Memlekete sis çökmüş bir gece 
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu'

Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve
bu string'i ekrana yazdırın."""

from sys import stdout
from time import sleep

while True:
    with open("siir.txt","r",encoding="utf-8") as file:

        a = file.read().split('\n')

        for i in a: 
            sleep(0.15)
            stdout.write(i[0])
            stdout.flush()
            """print(i[0])"""
    sleep(5)
    break
