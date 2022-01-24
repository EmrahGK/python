#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.


print("""**********************************

        EN BÜYÜK SAYI??

**********************************""")

a = int(input("ilk sayıyı girin: "))
b = int(input("ikinci sayıyı girin: "))
c = int(input("üçüncü sayıyı girin: "))


while True:
        
    if(a > b and a > c):
        print("girdiğiniz sayılardan en büyük olanı: ", a)
        break   

    elif(b > a and b > c):
        print("girdiğiniz sayılardan en büyük olanı: ", b)
        break


    elif(c > a and c > b):
        print("girdiğiniz sayılardan en büyük olanı: ", c)
        break

