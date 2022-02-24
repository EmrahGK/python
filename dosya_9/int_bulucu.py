"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.
 
liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
Bunu yaparken try,except bloklarını kullanmayı unutmayın."""

eleman1 = input("Birinci eleman: ")
eleman2 = input("İkinci eleman: ")
eleman3 = input("Üçüncü eleman: ")
eleman4 = input("Dördüncü eleman: ")
eleman5 = input("Beşinci eleman")

# kendime not: eleman1 = index olarak 0'dır
liste = [eleman1,eleman2,eleman3,eleman4,eleman5]

for i in liste:

    try:
        i = int(i)
        print(i)
    except:
        continue
