try:
    import requests as req
    from bs4 import BeautifulSoup
    
except:
    print("Modüllerin yüklenmesinde bir hata meydana geldi. Lütfen tekrar deneyin..")

sys_passwd = "8050916055063263178"

passwd = input("Lütfen şifreyi girin: ")


url= "https://emrahguvenkaya.glitch.me/index.html"
response = req.get(url)


content = response.content
soup = BeautifulSoup(content,"html.parser")


for i in soup.find_all("div"):
    print(i)
    print("**************************************************")












