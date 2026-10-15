"""
STUDI KASUS 3 - SISTEM KEAMANAN AKUN & AUDIT LOG LOGIN
Konsep yang digunakan: OOP (Class User), @property, RegEx (re), Decorator
"""

import re
from datetime import datetime


# =============================================================================
# REGEX PATTERN untuk validasi (sesuai requirement soal)
# =============================================================================
# Username: minimal 5 karakter, HANYA huruf & angka (alfanumerik), TANPA spasi
# Pola: ^[a-zA-Z0-9]{5,}$
USERNAME_PATTERN = r"^[a-zA-Z0-9]{5,}$"

# Password: minimal 8 karakter, WAJIB mengandung minimal SATU angka
# Penjelasan pola:
#   ^         = awal string
#   (?=.*\d)  = positive lookahead: pastikan ada angka (\d) di mana saja
#   .{8,}$    = sembarang karakter, minimal 8, sampai akhir
PASSWORD_PATTERN = r"^(?=.*\d).{8,}$"


# =============================================================================
# DATABASE SEDERHANA untuk simulasi autentikasi user yang terdaftar
# =============================================================================
DATABASE_USER = {
    "admin123": "admin1234",   # username valid, password valid (ada angka, 8 char)
    "dinda567": "dinda2024",   # username valid, password valid
}


# =============================================================================
# DECORATOR UNTUK AUDIT LOG (logika logging TERPISAH dari autentikasi)
# -----------------------------------------------------------------------------
# Decorator ini akan MEMBUNGKUS fungsi autentikasi dan otomatis mencatat
# setiap percobaan login ke audit_log beserta:
#   - timestamp/waktu
#   - username
#   - status BERHASIL / DITOLAK
#   - alasan penolakan (jika gagal)
#
# Ini memenuhi syarat: logika autentikasi utama TIDAK dipenuhi kode logging.
# =============================================================================
audit_log = []  # List untuk menyimpan semua riwayat login


def audit_login(func):
    """Decorator untuk audit logging otomatis setiap percobaan login."""
    def wrapper(username, password):
        # Dapatkan waktu saat ini SEBELUM login di-proses
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Panggil fungsi autentikasi ASLI yang dibungkus
        login_berhasil, alasan = func(username, password)

        # Status untuk log
        status = "BERHASIL" if login_berhasil else "DITOLAK"

        # Simpan ke audit log
        catatan = {
            "timestamp": timestamp,
            "username": username,
            "status": status,
            "alasan": alasan,
        }
        audit_log.append(catatan)

        # CETAK log ke terminal agar terlihat jelas
        print(f"  [AUDIT LOG] {timestamp} | User: {username:<15} | Status: {status:<9} | {alasan}")

        # Kembalikan hasil asli fungsi autentikasi
        return login_berhasil, alasan
    return wrapper


# =============================================================================
# CLASS USER dengan @property (enkapsulasi) + validasi RegEx
# =============================================================================
class User:
    """
    Class User yang mengenkapsulasi username dan password menggunakan @property.
    Validasi dilakukan di setter dengan module re (RegEx).
    """

    def __init__(self, username="", password=""):
        # Private attribute (konvensi _nama)
        self._username = ""
        self._password = ""
        # Set melalui property agar langsung tervalidasi
        if username:
            self.username = username
        if password:
            self.password = password

    # ------------------------------------------------------------------
    # Property USERNAME (getter + setter dengan validasi RegEx)
    # ------------------------------------------------------------------
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, nilai):
        """Validasi username menggunakan RegEx: min 5 char, alfanumerik saja."""
        if re.fullmatch(USERNAME_PATTERN, nilai):
            self._username = nilai
        else:
            raise ValueError(
                "Username tidak valid: minimal 5 karakter, hanya boleh huruf dan angka, "
                "tidak boleh spasi dan simbol."
            )

    # ------------------------------------------------------------------
    # Property PASSWORD (getter + setter dengan validasi RegEx)
    # ------------------------------------------------------------------
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, nilai):
        """Validasi password menggunakan RegEx: min 8 char, wajib ada angka."""
        if re.fullmatch(PASSWORD_PATTERN, nilai):
            self._password = nilai
        else:
            # Tentukan alasan spesifik agar pesan jelas
            if len(nilai) < 8:
                raise ValueError("Password tidak valid: minimal 8 karakter.")
            if not re.search(r"\d", nilai):
                raise ValueError("Password tidak valid: wajib mengandung minimal satu angka.")
            raise ValueError("Password tidak valid.")

    def __repr__(self):
        return f"User(username='{self.username}')"


# =============================================================================
# FUNGSI AUTENTIKASI UTAMA yang DIBUNGKUS DECORATOR @audit_login
# -----------------------------------------------------------------------------
# Perhatikan: di fungsi ini TIDAK ADA kode logging sama sekali.
# Logging dilakukan OTOMATIS oleh decorator di atas.
# =============================================================================
@audit_login
def proses_login(username, password):
    """
    Fungsi autentikasi utama: memeriksa username & password terhadap database.
    RETURN: tuple (berhasil: bool, alasan: str)
    """
    # --- VALIDASI FORMAT USERNAME DENGAN REGEX ---
    if not re.fullmatch(USERNAME_PATTERN, username):
        if len(username) < 5:
            return False, "Username terlalu pendek (minimal 5 karakter)."
        if " " in username:
            return False, "Username tidak boleh mengandung spasi."
        if not re.match(r"^[a-zA-Z0-9]+$", username):
            return False, "Username hanya boleh huruf dan angka (tidak boleh simbol)."
        return False, "Format username tidak valid."

    # --- VALIDASI FORMAT PASSWORD DENGAN REGEX ---
    if not re.fullmatch(PASSWORD_PATTERN, password):
        if len(password) < 8:
            return False, "Password terlalu pendek (minimal 8 karakter)."
        if not re.search(r"\d", password):
            return False, "Password tidak mengandung angka (wajib ada minimal satu angka)."
        return False, "Format password tidak valid."

    # --- CEK KE DATABASE ---
    if username not in DATABASE_USER:
        return False, "Username tidak terdaftar di sistem."
    if DATABASE_USER[username] != password:
        return False, "Password salah."

    # --- SEMUA LOLOS ---
    return True, "Login sukses: kriteria username & password terpenuhi."


# =============================================================================
# FUNGSI PENGUJIAN (Test Scenario sesuai soal)
# =============================================================================
def jalankan_test(nomor_test, nama_test, username, password):
    """Helper untuk menjalankan satu test scenario dan menampilkan output."""
    print("-" * 90)
    print(f"  TEST {nomor_test}: {nama_test}")
    print(f"  Input -> Username: '{username}' | Password: '{password}'")
    print("-" * 90)
    berhasil, alasan = proses_login(username, password)
    hasil_str = "[BERHASIL]" if berhasil else "[GAGAL]"
    print(f"  Hasil: {hasil_str}")
    print(f"  Info:  {alasan}")

    # Tambahan: Coba gunakan Class User untuk menunjukkan @property dan validasi
    try:
        user_obj = User(username, password)
        print(f"  Class User instansiasi: BERHASIL -> {user_obj}")
    except ValueError as e:
        print(f"  Class User instansiasi: GAGAL    -> {e}")
    print()


def main():
    print("=" * 90)
    print(f"{'SISTEM KEAMANAN AKUN & AUDIT LOG LOGIN':^90}")
    print("=" * 90)
    print(f"  Regex Username : {USERNAME_PATTERN}")
    print(f"                   (min 5 karakter, huruf & angka saja, tanpa spasi/simbol)")
    print(f"  Regex Password : {PASSWORD_PATTERN}")
    print(f"                   (min 8 karakter, wajib ada minimal 1 angka)")
    print(f"  Database User  : {list(DATABASE_USER.keys())}")
    print()
    print(f"  FYI: Decorator @audit_login otomatis mencatat setiap percobaan login.")
    print("=" * 90)
    print()

    # =========================================================================
    # 4 SKENARIO TEST SESUAI REQUIREMENT SOAL
    # =========================================================================
    print("=" * 90)
    print(f"{'SEKSI PENGUJIAN (4 SKENARIO WAJIB)':^90}")
    print("=" * 90)
    print()

    # TEST 1: Login gagal karena username tidak memenuhi format
    # Misal username terlalu pendek / ada spasi / ada simbol
    jalankan_test(
        nomor_test=1,
        nama_test="Username tidak memenuhi aturan format (ada simbol @)",
        username="admin@123",    # ada simbol '@' -> tidak sesuai RegEx alfanumerik
        password="admin1234"
    )

    # TEST 2: Login gagal karena password terlalu pendek (< 8 karakter)
    jalankan_test(
        nomor_test=2,
        nama_test="Password terlalu pendek (kurang dari 8 karakter)",
        username="admin123",
        password="admin1"      # hanya 6 karakter
    )

    # TEST 3: Login gagal karena password tidak mengandung angka
    jalankan_test(
        nomor_test=3,
        nama_test="Password tidak mengandung angka",
        username="admin123",
        password="adminpass"   # 9 karakter tapi TIDAK ada angka
    )

    # TEST 4: Login SUKSES karena seluruh kriteria terpenuhi
    jalankan_test(
        nomor_test=4,
        nama_test="SELURUH KRITERIA TERPENUHI (Login sukses)",
        username="admin123",
        password="admin1234"   # username ada di DB, password valid
    )

    # =========================================================================
    # TAMPILKAN RINGKASAN AUDIT LOG (semua percobaan)
    # =========================================================================
    print("=" * 90)
    print(f"{'RINGKASAN AUDIT LOG (SEMPURNA, TERURUT)':^90}")
    print("=" * 90)
    print(f"{'NO':<4}{'WAKTU':<22}{'USERNAME':<18}{'STATUS':<10}{'ALASAN'}")
    print("-" * 90)
    for i, log in enumerate(audit_log, start=1):
        print(f"{i:<4}{log['timestamp']:<22}{log['username']:<18}{log['status']:<10}{log['alasan']}")
    print("-" * 90)
    total = len(audit_log)
    berhasil = sum(1 for l in audit_log if l["status"] == "BERHASIL")
    gagal = total - berhasil
    print(f"Total percobaan: {total}  |  Berhasil: {berhasil}  |  Ditolak: {gagal}")
    print()

    # =========================================================================
    # DEMO CLASS USER dengan @property (buktikan enkapsulasi + validasi setter)
    # =========================================================================
    print("=" * 90)
    print(f"{'DEMO CLASS USER DENGAN @PROPERTY DAN VALIDASI REGEX':^90}")
    print("=" * 90)

    print("\n  [A] Membuat User dengan username & password VALID:")
    try:
        user_valid = User()
        user_valid.username = "dinda567"
        user_valid.password = "dinda2024"
        print(f"     User berhasil dibuat: username='{user_valid.username}'")
    except ValueError as e:
        print(f"     Error: {e}")

    print("\n  [B] Mencoba set username dengan SPASI (harus error):")
    user_coba = User()
    try:
        user_coba.username = "dinda 567"
        print(f"     Username: '{user_coba.username}'")
    except ValueError as e:
        print(f"     ValueError tertangkap (benar): {e}")

    print("\n  [C] Mencoba set password TANPA ANGKA (harus error):")
    try:
        user_coba.password = "dindacantik"
        print(f"     Password: '{user_coba.password}'")
    except ValueError as e:
        print(f"     ValueError tertangkap (benar): {e}")

    print()
    print("=" * 90)
    print(f"{'PROGRAM SELESAI':^90}")
    print("=" * 90)


if __name__ == "__main__":
    main()
