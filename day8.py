def apakah_prima(bilangan):
    if bilangan > 1:
        for i in range (2, int(bilangan ** 0.5 + 1)):
            if (bilangan % i) == 0 :
                return"bukan bilangan prima"
        else:
            return"bilangan prima"
    else: return"bukan bilangan prima"

bilangan = int(input("Masukkan bilagan: "))
hasil = apakah_prima(bilangan)
print(hasil)
