import os
import random

class FilmManager:
    def _init_(self):
        # Daftar film yang tersedia
        self.film_list = [
            "The Shawshank Redemption",
            "The Godfather",
            "The Dark Knight",
            "Schindler's List",
            "Pulp Fiction",
            "The Lord of the Rings: The Return of the King",
            "Transformers Dark of the Moon",
            "Inception",
            "Spider-Man No Way Home",
            "The Matrix"
        ]
    
    # Menyimpan daftar film ke file
    def simpan_daftar_film(self):
        # Cek apakah folder 'data' ada, jika belum buat folder
        if not os.path.exists("data"):
            os.makedirs("data")
        
        # Menyimpan daftar film ke file 'film_list.txt' di dalam folder 'data'
        with open("data/film_list.txt", "w") as file:
            for film in self.film_list:
                file.write(film + "\n")
        print("Daftar film telah disimpan di 'data/film_list.txt'")

    # Memilih film secara acak
    def pilih_film_acak(self):
        film_terpilih = random.choice(self.film_list)
        print(f"Film yang dipilih secara acak: {film_terpilih}")
    
    # Menampilkan semua film dalam daftar
    def tampilkan_daftar_film(self):
        print("Daftar Film:")
        for film in self.film_list:
            print(f"- {film}")

# Fungsi utama untuk interaksi dengan pengguna
def main():
    film_manager = FilmManager()

    while True:
        print("\nMenu:")
        print("1. Simpan daftar film ke file")
        print("2. Pilih film acak")
        print("3. Tampilkan daftar film")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            film_manager.simpan_daftar_film()
        elif pilihan == "2":
            film_manager.pilih_film_acak()
        elif pilihan == "3":
            film_manager.tampilkan_daftar_film()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Jalankan program
main()