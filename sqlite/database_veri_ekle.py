import time
import sqlite3

con = sqlite3.connect("veritabanı.db")

cursor = con.cursor()


def olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_sayısı INT) ")
    con.commit()

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(a,b,c,d):
    print("(Çıkmak için q'ya basın.)")
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(a,b,c,d))
    con.commit()

def cikis(x):
    try:
        x = str(x)
    except:
        print("HATAM TATATAM!")

    if(x == "q"):
        print("çıkılıyor..")
        return True
    else:
        return False
        
while True:
        
    kitap_isim = input("Kitap ismi: ")
    if(cikis(kitap_isim)):
        time.sleep(1)
        break
    kitap_yazar = input("Kitap Yazarı: ")
    if(cikis(kitap_yazar)):
        time.sleep(1)
        break
    kitap_yayınevi = input("Yayınevi: ")
    if(cikis(kitap_yayınevi)):
        time.sleep(1)
        break
    kitap_sayfa_sayisi = input("Sayfa sayısı: ")
    if(cikis(kitap_sayfa_sayisi)):
        time.sleep(1)
        break

    olustur()
    veri_ekle()

    if(kitap_isim == "q" or kitap_yazar == "q" or kitap_yayınevi == "q" or kitap_sayfa_sayisi == "q"):
        print("Programdan çıkılıyor...")
        time.sleep(2)
        quit()
        

    veri_ekle2(kitap_isim,kitap_yazar,kitap_yayınevi,kitap_sayfa_sayisi)

con.close()