
let input_list = []

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })
  
ad = readline.question(`Ad: `, name => {
    readline.close()
    return ad
})

soyad = readline.question(`Ad: `, name => {
    readline.close()
    return ad
})

yas = readline.question(`Ad: `, name => {
    readline.close()
    return ad
})
  
function yazdir (liste){
    text = 'Kullanıcının:\nAdı: ${ad}\nSoyadı: ${soyad}\nYaşı: ${yas}'
    console.log(text)
}
    





  



