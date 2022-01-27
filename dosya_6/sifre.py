
from distutils.util import check_environ


print("""
--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-
--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-

   Şifreleyici ve Şifreyi Çözücü Program
        (çıkmak için q'ya basın)


            İşlemler:
                1.Şifrele
                2.Şifreyi çöz

--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-
--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽-

""")

normal = "abcçdefgğhıijklmnoöprsştuüvyz"
encrypted = "bcçdefgğhıijklmnoöprsştuüvyza"

cevir = str.maketrans(normal,encrypted)
coz = str.maketrans(encrypted,normal)

while True:
    
    islem = str(input("İşlemi girin (1-2): "))

    if(islem == "1"):

        metin = str(input("Şifrelenmesini istediğiniz metni girin: "))
        print("Şifrelenmiş metin: ",metin.translate(cevir))

    elif(islem == "2"):
        metin = str(input("Şifresinin çözülmesini istediğiniz metni girin: "))
        print("Şifrelenmiş metin: ",metin.translate(coz))