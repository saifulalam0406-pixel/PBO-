# CASE 03 — SISTEM KEAMANAN AKUN & AUDIT LOG LOGIN

## 1. Ringkasan Masalah
Sistem login yang baik tidak hanya melakukan autentikasi username dan password, tetapi juga harus:
1. Memvalidasi format input sebelum dicek ke database (mencegah input invalid masuk lebih jauh).
2. Mencatat seluruh riwayat percobaan login (audit trail) untuk keperluan keamanan.
3. Memisahkan kode logging dari logika autentikasi agar tidak berantakan dan mudah dipelihara.

Studi kasus ini mengimplementasikan ketiga hal tersebut dengan memanfaatkan fitur OOP, `@property`, Regular Expression (RegEx), dan Decorator di Python.

## 2. Tujuan Program
- Membuat **Class `User`** yang mengenkapsulasi `username` dan `password` melalui dekorator **`@property`** (getter & setter).
- Melakukan validasi `username` dan `password` secara ketat menggunakan **module `re` (RegEx)**.
- Membuat **Decorator / Closure** `@audit_login` yang secara otomatis melakukan audit logging setiap percobaan login, sehingga logika autentikasi tetap bersih.
- Audit log wajib mencatat: **timestamp**, **username**, **status (BERHASIL / DITOLAK)**, dan **alasan penolakan** jika gagal.
- Menjalankan 4 skenario uji yang ditentukan soal dan menampilkan seluruh riwayat audit log secara terurut.

## 3. Konsep Python yang Digunakan
| Konsep | Keterangan Penerapan |
|--------|----------------------|
| **OOP (Class `User`)** | Mendefinisikan entitas User beserta perilaku validasinya. |
| **`@property`** | Getter & setter untuk `username` dan `password`. Validasi RegEx terjadi di setter, sehingga assignment seperti `user.username = "admin"` akan langsung memicu validasi. |
| **Regular Expression (`re`)** | `re.fullmatch(USERNAME_PATTERN, ...)` dan `re.fullmatch(PASSWORD_PATTERN, ...)` untuk memeriksa format input dengan presisi. |
| **Decorator `@audit_login`** | Membungkus fungsi `proses_login()` agar kode logging (timestamp, status, alasan) dijalankan otomatis sebelum/sesudah autentikasi, tanpa mengotori kode autentikasi itu sendiri. |
| **List `audit_log`** | Menyimpan semua catatan login yang kemudian ditampilkan sebagai ringkasan. |

## 4. Penjelasan Singkat Aturan Validasi (RegEx)
```
USERNAME_PATTERN = r"^[a-zA-Z0-9]{5,}$"
- ^         : awal string
- [a-zA-Z0-9] : HANYA karakter a-z, A-Z, 0-9  (alfanumerik, TANPA simbol & spasi)
- {5,}      : minimal 5 karakter
- $         : akhir string

PASSWORD_PATTERN = r"^(?=.*\d).{8,}$"
- (?=.*\d)  : Positive lookahead — pastikan ADA MINIMAL 1 ANGKA (\d) di mana saja
- .{8,}     : sembarang karakter, MINIMAL 8 huruf
```

## 5. Penjelasan Singkat Cara Kerja Program
1. **Pembuatan Class User**:
   - Attribute privat `_username` dan `_password`.
   - `@property username.setter` memakai `re.fullmatch(USERNAME_PATTERN, nilai)`. Jika tidak cocok → raise `ValueError`.
   - `@property password.setter` memakai `re.fullmatch(PASSWORD_PATTERN, nilai)`. Jika tidak cocok → raise `ValueError` dengan pesan yang relevan (kurang panjang / tidak ada angka).
2. **Decorator `@audit_login`**:
   - Membungkus fungsi `proses_login()`.
   - Sebelum autentikasi: ambil `timestamp` sekarang.
   - Jalankan fungsi autentikasi asli → dapatkan `(berhasil, alasan)`.
   - Simpan 4 field (timestamp, username, status, alasan) ke list `audit_log`.
   - Cetak baris log ke terminal.
   - Kembalikan hasil asli fungsi autentikasi ke pemanggil.
3. **4 Skenario Uji Wajib** via fungsi pembantu `jalankan_test()`:
   - TEST 1: Username `admin@123` (ada simbol `@`) → ditolak.
   - TEST 2: Password `admin1` (6 karakter) → ditolak.
   - TEST 3: Password `adminpass` (tidak ada angka) → ditolak.
   - TEST 4: Username `admin123` + password `admin1234` → BERHASIL.
4. **Ringkasan Audit Log**: Semua 4 percobaan ditampilkan kembali dalam tabel lengkap.
5. **Demo Class User**: Membuat User dengan input valid & invalid untuk membuktikan setter `@property` + RegEx bekerja.

## 6. Struktur / File yang Digunakan
```
case-03-login-security/
├── main.py       # Program utama: Class User, RegEx, Decorator, & Skenario Test
├── README.md     # Dokumentasi ini
└── output.png    # Screenshot output terminal
```

## 7. Cara Menjalankan Program
```bash
cd case-03-login-security
python main.py
```
Atau dari root project:
```bash
python case-03-login-security/main.py
```

## 8. Contoh Output (Ringkasan)
```
==========================================================================================
                     SISTEM KEAMANAN AKUN & AUDIT LOG LOGIN
==========================================================================================

------------------------------------------------------------------------------------------
  TEST 1: Username tidak memenuhi aturan format (ada simbol @)
  Input -> Username: 'admin@123' | Password: 'admin1234'
------------------------------------------------------------------------------------------
  [AUDIT LOG] 2026-10-06 21:00:00 | User: admin@123       | Status: DITOLAK  | Username hanya boleh huruf dan angka (tidak boleh simbol).
  Hasil: ✗ GAGAL
  Class User instansiasi: GAGAL    -> Username tidak valid: ...

  TEST 2: Password terlalu pendek (kurang dari 8 karakter)
  Input -> Username: 'admin123' | Password: 'admin1'
------------------------------------------------------------------------------------------
  [AUDIT LOG] 2026-10-06 21:00:00 | User: admin123        | Status: DITOLAK  | Password terlalu pendek (minimal 8 karakter).

  TEST 3: Password tidak mengandung angka
------------------------------------------------------------------------------------------
  [AUDIT LOG] 2026-10-06 21:00:00 | User: admin123        | Status: DITOLAK  | Password tidak mengandung angka ...

  TEST 4: SELURUH KRITERIA TERPENUHI (Login sukses)
------------------------------------------------------------------------------------------
  [AUDIT LOG] 2026-10-06 21:00:00 | User: admin123        | Status: BERHASIL | Login sukses: kriteria username & password terpenuhi.
  Hasil: ✓ BERHASIL

==========================================================================================
                          RINGKASAN AUDIT LOG
==========================================================================================
NO  WAKTU                  USERNAME          STATUS    ALASAN
------------------------------------------------------------------------------------------
1   2026-10-06 21:00:00   admin@123         DITOLAK   Username hanya boleh huruf dan angka...
2   2026-10-06 21:00:00   admin123          DITOLAK   Password terlalu pendek...
3   2026-10-06 21:00:00   admin123          DITOLAK   Password tidak mengandung angka...
4   2026-10-06 21:00:00   admin123          BERHASIL  Login sukses: kriteria username & password terpenuhi.
Total percobaan: 4  |  Berhasil: 1  |  Ditolak: 3
```

## 9. Penjelasan Requirement yang Sudah Dipenuhi
| Requirement Soal | Status |
|------------------|--------|
| **Class `User`** dibuat | ✅ Ada, dengan konstruktor `__init__` dan `__repr__` |
| **`@property`** untuk username & password | ✅ Getter + setter untuk keduanya |
| Username: min 5 karakter, huruf+angka saja, tanpa spasi/simbol | ✅ `USERNAME_PATTERN = r"^[a-zA-Z0-9]{5,}$"` + setter validasi |
| Password: min 8 karakter, wajib ada angka | ✅ `PASSWORD_PATTERN = r"^(?=.*\d).{8,}$"` + setter validasi |
| Validasi **menggunakan RegEx (`re`)** | ✅ `re.fullmatch()` di setter & di `proses_login()` |
| **Decorator / Closure** audit logging | ✅ `@audit_login` decorator (bisa juga disebut closure) |
| Logging otomatis setiap percobaan login | ✅ Dipanggil otomatis lewat decorator, tak perlu panggil manual |
| Audit log: timestamp, username, status BERHASIL/DITOLAK, alasan penolakan | ✅ Semua 4 field disimpan & ditampilkan |
| Logika autentikasi TIDAK berantakan logging | ✅ `proses_login()` HANYA berisi validasi & cek DB. Logging DI decorator. |
| TEST 1: Username format invalid | ✅ `admin@123` (simbol) |
| TEST 2: Password terlalu pendek | ✅ `admin1` (6 char) |
| TEST 3: Password tanpa angka | ✅ `adminpass` (0 angka) |
| TEST 4: Login SUKSES | ✅ `admin123`/`admin1234` (user di DB, format valid) |
| Output jelas tiap percobaan + audit log | ✅ Ada tabel ringkasan |
