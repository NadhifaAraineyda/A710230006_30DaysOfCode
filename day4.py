nama_depan = input("nama depan : ")
nama_belakang = input("nama belakang : ")
NIM = input("NIM : ")
nama_lengkap = nama_depan + ("") + nama_belakang
print("")

kata_prodi = "Pendidikan Teknik Informatika"
kata_fakultas = "Fakultas Keguruan dan Ilmu Pendidikan"
kata_universitas = "Universitas Muhammadiyah Surakarta"

print(kata_prodi.center(60))
kapital = kata_universitas.upper()
print(" ")
print("nama {}".format(nama_lengkap))
print("NIM {}".format(NIM))
print("{}".format(kata_fakultas))
print(" ")
print(kapital.center(60))
