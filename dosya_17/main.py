"""
collatz problemi: sayı çift ise ikiye böl, sayı tek ise 3 ile çarpıp 1 ekle şeklinde ilerleyen problem.

x sayısı için her zaman 8.4.2.1 olarak biter

x .., .., .., .., .., 8, 4, 2, 1. gibi

mesela sayı 3 ise;

3 bir tek sayı olduğu için 3.3 + 1 'den 10.
10 çift sayı olduğu için 10/2'den 5.
5 tek sayı olduğu için 5.3+1'den 16
16/2'den 8 
8/2'den 4
4/2'den 2
2/2'den 1 olarak sonuç çıkar

bu programın yazılış amacı, x sayısı için bu işlemleri yapacak bir algoritma yazmak. bunun için yapılacak en temel
şey, sayının çift mi tek mi olduğunu gösteren bir fonksiyon yazmak. gerisi beleş 

"""

def status(sayi):

    kalan = sayi %2
    if(kalan == 0): #sayi çift ise
        return True
    elif(kalan==1): #sayi tek ise
        return False
    else:
        print("HATA!!!!")

print("""
___________________________________

        COLLATZ PROBLEMİ
    (çıkmak için q'ya basın)
___________________________________

""")


while True:

    sayı = input("Lütfen sayıyı girin.")

    liste = []




