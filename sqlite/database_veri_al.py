import time
import sqlite3

con = sqlite3.connect("veritabanı.db")

cursor = con.cursor()


def olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_sayısı INT) ")
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
def veri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()        
    print(liste)

con.close()