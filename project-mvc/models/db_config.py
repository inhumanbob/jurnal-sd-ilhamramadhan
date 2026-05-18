import os
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env yang ada di root folder
load_dotenv()

# Mengambil nilai kredensial secara aman
db_password = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")

# Simulasi inisialisasi koneksi database (Hanya untuk contoh)
def connect_db():
    if db_password:
        return "Koneksi ke database berhasil diinisialisasi secara aman."
    else:
        return "Gagal: Kredensial database tidak ditemukan!"

# Cek status
print(connect_db())