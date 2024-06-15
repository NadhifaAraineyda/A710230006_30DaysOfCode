def kasir_toko():
    total_harga = 0
    invoice_detail = ""
jumlah_barang = int(input("Masukkan jumlah barang: "))
for i in range(1, jumlah_barang + 1):
    nama_barang = input(f"Masukkan nama barang ke-{i}: ")
    harga_barang = float(input(f"Masukkan harga barang {nama_barang}: "))
    jumlah_barang = int(input(f"Masukkan jumlah {nama_barang} yang dibeli: "))
harga_total = harga_barang * jumlah_barang
total_harga = harga_barang * jumlah_barang
print("\nTotal Harga: Rp", total_harga)
with open("invoice.txt", "w") as file:
    file.write("Rincian Belanja:\n")
    file.write("\nTotal Harga: Rp "+ str(total_harga))
    print("Transaksi selesai. Rincian belanja telah disimpan di invoice.txt")
