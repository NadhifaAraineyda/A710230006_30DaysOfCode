class Orang:
    def __init__(self, nama, makanan_kesukaan, minuman_kesukaan, hobi):
        self.nama = nama
        self.makanan_kesukaan = makanan_kesukaan
        self.minuman_kesukaan = minuman_kesukaan
        self.hobi = hobi
    
    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}.")
        print(f"Hobi saya adalah {self.hobi}.")
        print(f"Saya suka makan {self.makanan_kesukaan}.")
        print(f"Minuman kesukaan saya adalah {self.minuman_kesukaan}.")

orang1 = Orang("John", "pizza", "kopi", "bersepeda")
orang2 = Orang("Jane", "sushi", "teh", "membaca")

orang1.perkenalan()
print()
orang2.perkenalan()