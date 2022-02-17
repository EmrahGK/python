const prompt = require("prompt-sync")({ sigint: true });


let input_list = []

ad = prompt("Adın ne? ")

soyad = prompt("Soyadını yuaz.. : ")

yas = prompt("Bu geçici dünyaya geldiğin yılı yazınız: ")
  
function yazdir (liste){
    text = `Kullanıcının:
    Adı: ${ad}\n
    Soyadı: ${soyad}\n
    Yaşı: ${yas}`
    console.log(text)
}

yazdir();





  



