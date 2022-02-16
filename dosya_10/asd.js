function bilgilerigoster(su){
    console.log("suyun ph değeri", su.ph);
    console.log("su miktarı: ",su.mililitre)
    su.ph = 8
    console.log("suyun yeni ph değeri", su.ph);
    

}

bilgilerigoster({
    ph: 7,
    mililitre: 500,
    marka: "sultan",
    kaynak_yeri:"uludağ",
    icindekiler: [
        {
            isim: "among us juice",
            miktar: 200
        },
        {
            isim: "h2o",
            miktar: 2848927389427
        }
    ]
});

// Suyun PH değeri: 7



