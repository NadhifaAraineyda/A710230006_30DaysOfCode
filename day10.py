class Mahasiswa:
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi

    def kartu_mahasiswa(self):
        print(f"Data Mahasiswa:\nNIM: {self.nim}\nNama: {self.nama}\nAngkatan: {self.angkatan}\nProdi: {self.prodi}")

    def selamat(self):
        print(f"Selamat Datang {self.nama} di kampus UMS")

mahasiswa1 = Mahasiswa("A710230006", "Nadhifa Araineyda", "2023", "PTI")
mahasiswa2 = Mahasiswa("A710230007", "Synta Nur", "2023", "PTI")
mahasiswa3 = Mahasiswa("A710230009", "Maya Mega", "2023", "PTI")

mahasiswa1.kartu_mahasiswa()
mahasiswa1.selamat()

mahasiswa2.kartu_mahasiswa()
mahasiswa2.selamat()

mahasiswa3.kartu_mahasiswa()
mahasiswa3.selamat()
