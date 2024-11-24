import os
import random

# Daftar film
film_list = [
    "Avengers: Endgame",
    "The Dark Knight",
    "Inception",
    "Forrest Gump",
    "Titanic",
    "The Matrix",
    "The Shawshank Redemption",
    "Interstellar",
    "Gladiator",
    "The Lion King"
]

# Fungsi untuk memilih film secara acak
def pilih_film():
    film_acak = random.choice(film_list)
    print(f"Film yang dipilih: {film_acak}")

# Fungsi untuk membuat direktori baru jika belum ada
def buat_direktori(direktori):
    if not os.path.exists(direktori):
        os.makedirs(direktori)
        print(f"Direktori '{direktori}' berhasil dibuat.")
    else:
        print(f"Direktori '{direktori}' sudah ada.")

# Fungsi untuk menulis pilihan film ke dalam file
def simpan_ke_file(film_terpilih):
    direktori = "film_terpilih"
    buat_direktori(direktori)
    
    # Menulis nama film yang dipilih ke dalam file
    file_path = os.path.join(direktori, "film.txt")
    with open(file_path, "a") as file:
        file.write(film_terpilih + "\n")
    print(f"Film '{film_terpilih}' disimpan dalam file '{file_path}'.")

# Program utama
pilih_film()  # Memilih film secara acak
film_terpilih = random.choice(film_list)  # Memilih film acak dari daftar
simpan_ke_file(film_terpilih)  # Menyimpan film terpilih ke file