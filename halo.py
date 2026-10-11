# halo.py - program Python dengan fitur hobi dan pewarnaan teks menggunakan colorama
from colorama import init, Fore, Style

# Inisialisasi colorama untuk Windows
init(autoreset=True)

print(Fore.CYAN + "=== Program Sapaan Praktikum Python ===")

# Meminta input dari pengguna
nama = input(Fore.YELLOW + "Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")
print(Fore.GREEN + "Semoga Anda menikmati belajar Python!")

umur = int(input(Fore.YELLOW + "Masukkan umur Anda: "))
print(Fore.MAGENTA + f"Tahun depan umur Anda {umur + 1} tahun.")

# Fitur tambahan: Menanyakan dan menampilkan hobi
hobi = input(Fore.YELLOW + "Masukkan hobi Anda: ")
print(Fore.BLUE + f"Wah, keren sekali! Hobi Anda adalah {hobi}.")
