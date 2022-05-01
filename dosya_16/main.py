# bu programın amacı matematiksel olasılığın deneysel olasılıkla olan ilişkisini test etmek için programlandı (fikri bana ait) 
# şimdilik yazı tura işlemini yapacağım ileride 1-100 arası sayılarla olan versionu da gelebilir.



liste = range(1,101)

soru = input("Hangi sayının çıkma olasılığını bulmak istiyorsunuz? (1-100): ")

try:
    soru = int(soru)
except:
    print("HATA!!!")

if(soru in liste):
    pass