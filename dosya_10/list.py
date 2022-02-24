input_list = ["None","None","None"]


ad = input("Ad: ")
soyad = input("Soyad: ")
yaş = input("Yaş: ")

input_list[0] = ad
input_list[1] = soyad
input_list[2] = yaş

def yazdir(liste):

    try:
        liste = list(liste)
    except:
        print("HATAAAA:::!:!:!:!:")

    print(f"""

    Kullanıcının:

    Adı: {liste[0]}

    Soyadı: {liste[1]}

    Yaşı: {liste[2]}

    """)

yazdir(input_list)






