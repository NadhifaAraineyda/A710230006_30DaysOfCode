class Tiket:
    def __init__(self, jumlah):
        self.jumlah = jumlah
    
    def hitung_harga(self):
        pass

class TiketBiasa(Tiket):
    def hitung_harga(self):
        return self.jumlah * 50000

class TiketVIP(Tiket):
    def hitung_harga(self):
        return self.jumlah * 75000

class TiketGold(Tiket):
    def hitung_harga(self):
        return self.jumlah * 100000

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ").lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jenis_tiket == 'biasa':
        tiket = TiketBiasa(jumlah_tiket)
    elif jenis_tiket == 'vip':
        tiket = TiketVIP(jumlah_tiket)
    elif jenis_tiket == 'gold':
        tiket = TiketGold(jumlah_tiket)
    else:
        print("Jenis tiket tidak valid.")
        return

    total_harga = tiket.hitung_harga()
    print("Total Harga Tiket: Rp", total_harga)

if __name__ == "__main__":
    main()