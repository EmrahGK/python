import time
print("""
_____________________________

        İŞ İLAN FORMU
_____________________________
""")   
print("""
\n
Öğrenim durumları:
    1.İlkokul
    2.Ortaokul
    3.Lise
    4.Ön Lisans
    5.Lisans
    6.Yüksek Lisans
    7.Doktora
    8.Diğer        
""")
class insan():
        def __init__(self,ad,soyad,maaş,öğrenim_durumu,şehir,kimlik_no):
            self.ad = ad
            self.soyad = soyad
            self.maaş = maaş
            self.öğrenim_durumu = öğrenim_durumu
            self.şehir = şehir
            self.kimlik_no = kimlik_no

        def bilgilerigöster(self):
            print("""
            Kullanıcının;

            Adı: {}

            Soyadı: {}

            Maaşı: {}

            Öğrenim durumu: {}

            Yaşadığı şehir: {}

            Kimlik Numarası: {}

            """.format(self.ad,self.soyad,self.maaş,self.öğrenim_durumu,self.şehir,self.kimlik_no))
while True:
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    maaş = input("Maaşınız: ")
    öğrenim_durumu = input("Öğrenim durumunuz: ")
    şehir = input("Yaşadığınız şehir: ")
    kimlik_no = input("T.C Kimlik No'nuzu girin: ")
    kimlik_no_uzunluk = len(kimlik_no)

    human = insan(ad,soyad,maaş,öğrenim_durumu,şehir,kimlik_no)

    try:
        kimlik_no = int(kimlik_no)
    except ValueError:
        print("\nLüfen geçerli bir kimlik numarası girin.")
        time.sleep(0.8)
        print("Ana menüye yönlendiriliyorsunuz..")
        time.sleep(1)
        continue
    
    try:
        maaş = int(maaş)
    except ValueError:
        print("\nLüfen geçerli bir maaş değeri girin.")
        time.sleep(0.8)
        print("Ana menüye yönlendiriliyorsunuz..")
        time.sleep(1)
        continue

    if(not kimlik_no_uzunluk == 11):
        time.sleep(1)
        print("Lüfen geçerli bir kimlik numarası girin.")
        time.sleep(0.8)
        print("Ana menüye yönlendiriliyorsunuz..")
        time.sleep(1)
        continue
    
    print("\nBilgileriniz işleniyor...")
    time.sleep(1.2)
    human.bilgilerigöster()