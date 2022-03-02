import json
import time
from os import path


print("""
_________________________________________________________



                   REGİSTER/LOGİN
       (hesabınız yoksa kendinize bir tane oluşturun.)

        İşlemler:

            1.Kayıt ol  
            2.Giriş yap

_________________________________________________________
""")



while True:

    print("\n\nHello Motherfucking World\n")
    islem = input("İşlemi girin: ")
    veriler = {}

    if islem == "q":
        print("Programdan çıkılıyor...")
        time.sleep(1.5)
        break
    
    elif(islem == "1"):
        usernameinput = input("Username :")
        passwdinput = input("Password :")
        mailinput = input("Mail :")
        phoneinput = input("Phone Number :")
        
        
        time.sleep(0.5)

        emin_mi = input("\nGirdiğin bilgileri doğruluyor musun? (y/n)")
        if(emin_mi == "y" or emin_mi=="Y"):
            with open("db.json") as fp:
                listObject = json.load(fp)
      
            listObject".append" = (f"""
                'username': {usernameinput},
                'password': {passwdinput},
                'mail': {mailinput},
                'phone': {phoneinput}"""
            )
            

        elif(emin_mi == "n" or emin_mi=="N"):
            print("Ana menüye yönlendiriliyorsunuz...")
            time.sleep(0.5)

            continue

    elif(islem =="2"):
        pass
    else:
        print("HATA!!!!")
        time.sleep(1)
        continue
