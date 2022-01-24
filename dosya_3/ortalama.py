#Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

#    Vize1 toplam notun %30'una etki edecek.

#    Vize2 toplam notun %30'una etki edecek.

#    Final toplam notun %40'ına etki edecek.


#    Toplam Not >=  90 -----> AA

#    Toplam Not >=  85 -----> BA

#    Toplam Not >=  80 -----> BB

#    Toplam Not >=  75 -----> CB

#    Toplam Not >=  70 -----> CC

#    Toplam Not >=  65 -----> DC

#    Toplam Not >=  60 -----> DD

#    Toplam Not >=  55 -----> FD

#    Toplam Not <  55 -----> FF




vize1 = float(input("birinci vize notunu girin: "))
vize2 = float(input("ikinci vize notutunu girin: "))
final = float(input("final notunuzu girin: "))

toplam = (vize1 * (3/10)) + (vize2 * (3/10)) + (final * (4/10))

#    Toplam Not >=  75 -----> CB

#    Toplam Not >=  70 -----> CC

#    Toplam Not >=  65 -----> DC

#    Toplam Not >=  60 -----> DD

#    Toplam Not >=  55 -----> FD

#    Toplam Not <  55 -----> FF

if(toplam >= 90):
    print("Tebrikler, AA aldınız.")

elif(85 <= toplam < 90):
    print("Tebrikler, BA aldınız.")

elif(80 <= toplam < 85):
    print("Tebrikler, BB aldınız.")

elif(75 <= toplam < 80):
    print("Tebrikler, CB aldınız.")

elif(70 <= toplam < 75):
    print("Tebrikler, CC aldınız.")

elif(65 <= toplam < 70):
    print("Tebrikler, DC aldınız.")

elif(60 <= toplam < 65):
    print("Tebrikler, DD aldınız.")

elif(55 <= toplam < 60):
    print("Tebrikler, FD aldınız.")

elif(toplam < 55):
    print("Maalesef FF aldınız..")