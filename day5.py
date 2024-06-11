tahun_lahir = int(input("Masukkan tahun lahir : "))
harga_tiket = int(input("Masukkan harga tiket : "))

usia = int(2023) + int(tahun_lahir)

if (usia >= 0 and usia <=4):
    diskon = harga_tiket * 100/100
    setelah_diskon = harga_tiket - diskon
    print("Karena usia 0-4 mendapatkan diskon 100%, Total Harganya yaitu :", setelah_diskon)

elif (usia >=5 and usia <=11):
    diskon = harga_tiket * 50/100
    setelah_diskon = harga_tiket - diskon
    print("Karena usia 5-11 mendapatkan diskon 50%, Total Harganya yaitu :", setelah_diskon)

else :
    print("Tidak mendapatkan diskon dikarenakan usia sudah diatas 11 tahun")