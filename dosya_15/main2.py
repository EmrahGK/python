sınır = 101
liste_sayı = range(sınır)
for x in liste_sayı:
    y = x - 1
    bolum = 0
    bolum = x % y
    try:
        bolum = float(bolum)
    except:
        print("HATAGÖTGÖT")
        break
    while bolum != 0:
        y = y - 1
        if y < 1 :
            print(x + "asal sayıdır.")
            continue
        bolum = x % y
        if bolum == 0:
            print(x + "asal sayı deildir.")
            continue
        
