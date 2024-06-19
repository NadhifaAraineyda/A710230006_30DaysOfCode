while True:
    try:
        # Meminta input dari user
        bilangan = int(input("Masukkan bilangan bulat: "))
        
        # Menghitung pangkat dua
        kuadrat = bilangan ** 2
        
        # Mencetak hasil
        print(f"Hasil pangkat dua dari {bilangan} adalah {kuadrat}")
        
        # Break loop jika input valid
        break
    except ValueError:
        # Menampilkan pesan error
        print("Input yang dimasukkan tidak valid!")