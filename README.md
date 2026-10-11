Isi File README.md
Buat file baru bernama README.md di dalam folder utama proyek Anda (PraktikumAldy-python), lalu salin dan tempel (paste) teks di bawah ini:

Markdown
# Praktikum Python - Aldy

Repositori ini berisi kumpulan kode dan latihan pemrograman menggunakan bahasa Python untuk keperluan praktikum.

---

## 1. Membuat dan Mengaktifkan Virtual Environment

Sebelum menjalankan program, sangat disarankan untuk menggunakan *virtual environment* agar dependensi proyek tetap terisolasi.

### Di Windows (Command Prompt / PowerShell):
1. **Membuat virtual environment** (bernama `.venv`):
   ```bash
   python -m venv .venv
Mengaktifkan virtual environment:

PowerShell:

Bash
.venv\Scripts\Activate.ps1
Command Prompt (CMD):

Bash
.venv\Scripts\activate.bat
2. Menginstal Dependensi
Jika proyek ini memiliki file requirements.txt, Anda dapat menginstal seluruh pustaka/dependensi yang dibutuhkan dengan perintah berikut:

Bash
pip install -r requirements.txt
(Pastikan virtual environment sudah dalam keadaan aktif saat menginstal dependensi).

3. Cara Menjalankan Program
Pastikan Anda berada di dalam folder proyek dan virtual environment sudah aktif ((.venv) muncul di awal baris terminal).

Jalankan file Python utama menggunakan perintah:

Bash
python nama_file.py
(Ganti nama_file.py dengan nama file yang ingin Anda jalankan, contoh: python halo.py)


---

### Cara Membuatnya Melalui VS Code:
1. Di panel *Explorer* (kiri atas VS Code), klik ikon **New File** (ikon kertas dengan tanda `+`).
2. Ketik nama file: `README.md`, lalu tekan **Enter**.
3. Tempel teks di atas ke dalam file tersebut, lalu simpan dengan menekan `Ctrl + S`.

Setelah file ini dibuat dan disimpan, Anda bisa langsung melakukan *commit* dan *push* ulang ke GitHb
