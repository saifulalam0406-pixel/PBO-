# Python Advanced Case Study

## 1. Identitas Mahasiswa
> ⚠️ Silakan **edit bagian ini** sebelum mengumpulkan. **JANGAN biarkan kosong / templatenya saja**.

| Data | Isi |
|------|-----|
| **Nama**  | `(Isi nama lengkap Anda)` |
| **NIM**   | `(Isi NIM Anda)` |
| **Kelas** | `(Isi kelas / prodi Anda)` |

> Catatan: Template ini sengaja disediakan tanpa mengarang identitas sesuai perintah soal.

---

## 2. Ringkasan Ketiga Studi Kasus
Repository ini berisi implementasi tiga studi kasus yang menguji penguasaan konsep-konsep Python tingkat lanjut.

### 📘 Case 01 — Analisis Nilai Mahasiswa
**Folder**: `case-01-analisis-nilai/`

Program yang menerima data daftar mahasiswa (nama, NIM, nilai tugas, UTS, UAS) lalu:
- Menghitung nilai akhir dengan bobot Tugas 30% + UTS 30% + UAS 40%.
- Menyaring mahasiswa berprestasi (nilai akhir > 80).
- Membuat ranking mahasiswa dari nilai tertinggi ke terendah.
- Menampilkan mahasiswa terbaik (peringkat 1).

### 📗 Case 02 — Streaming Data Sensor IoT
**Folder**: `case-02-iot-generator/`

Simulasi streaming data pembacaan sensor suhu ruangan dengan konsep **Generator**:
- Generator function dengan `yield` menghasilkan data suhu satu per satu (15°C–38°C).
- Didesain hemat memori: tidak ada list besar penyimpanan seluruh data.
- Dikonsumsi bertahap via `next()` eksplisit dan via for-loop.
- Setiap pembacaan langsung dikategorikan: Dingin / Normal / Panas.

### 📕 Case 03 — Sistem Keamanan Akun & Audit Log Login
**Folder**: `case-03-login-security/`

Implementasi sistem login yang aman dan teraudit:
- Class `User` dengan `@property` untuk enkapsulasi username & password.
- Validasi format username & password menggunakan **RegEx (module `re`)**.
- **Decorator `@audit_login`** untuk logging otomatis (terpisah dari logika autentikasi).
- Audit log mencatat waktu, username, status BERHASIL/DITOLAK, dan alasan penolakan.
- Diuji dengan 4 skenario yang ditentukan soal.

---

## 3. Konsep Python yang Digunakan Keseluruhan
Berikut adalah konsep-konsep Python tingkat lanjut yang digunakan beserta lokasi penerapannya.

| Konsep | Keterangan | Lokasi Penerapan |
|--------|------------|------------------|
| **List Comprehension** | Membangun list baru `daftar_nilai` secara ringkas dari `data_mahasiswa`. | Case 01 – `main.py` baris ~40 |
| **Lambda Function** | Fungsi anonim sebagai `key` di `filter()` dan `sorted()`. | Case 01 – `filter(lambda m: m[...])` & `sorted(key=lambda m: m[...])` |
| **Filtering** | Menyaring record dengan `filter()` berdasarkan kriteria. | Case 01 – mahasiswa nilai akhir > 80 |
| **Sorting** | Mengurutkan data secara menurun pakai `sorted(..., reverse=True)`. | Case 01 – ranking mahasiswa |
| **Generator** | Fungsi khusus yang menghasilkan nilai bertahap dengan `yield`. | Case 02 – `sensor_suhu_generator()` |
| **Iterator** | Mengambil data generator satu per satu pakai `next()` dan `iter()`. | Case 02 – Demo 1 `next(iterator_1)` |
| **Keyword `yield`** | Jantung generator: mengembalikan nilai sambil menahan state fungsi. | Case 02 – `yield nomor, suhu` |
| **Regular Expression (RegEx)** | Pola validasi string presisi pakai module `re`. | Case 03 – `USERNAME_PATTERN` & `PASSWORD_PATTERN` |
| **Decorator / Closure** | Membungkus fungsi untuk menambah perilaku (logging) secara terpisah. | Case 03 – `@audit_login` di atas `proses_login()` |
| **`@property`** | Getter + setter untuk atribut kelas dengan validasi. | Case 03 – `User.username` dan `User.password` setter |
| **OOP (Class & Object)** | Pendefinisian Class `User` dan instansiasi objeknya. | Case 03 – `class User`, `User()`, setter property |

---

## 4. Cara Menjalankan Setiap Program
Pastikan Python 3.8+ sudah terinstal. Buka terminal di **root folder project** (`python-advanced-case-study/`), lalu jalankan:

| Studi Kasus | Perintah |
|-------------|----------|
| **Case 01 – Analisis Nilai** | `python case-01-analisis-nilai/main.py` |
| **Case 02 – IoT Generator**  | `python case-02-iot-generator/main.py` |
| **Case 03 – Login Security** | `python case-03-login-security/main.py` |

> Catatan: Semua program **TIDAK membutuhkan library eksternal** (hanya menggunakan built-in module: `random`, `time`, `re`, `datetime`). Tidak perlu `pip install` apa pun.

---

## 5. Struktur Repository
Berikut adalah struktur file lengkap repository ini (sesuai ketentuan soal):

```
python-advanced-case-study/
│
├── README.md                                   # README UTAMA (file ini)
│
├── case-01-analisis-nilai/                     # STUDI KASUS 1
│   ├── main.py                                 # Program utama Case 01
│   ├── README.md                               # Dokumentasi Case 01
│   └── output.png                              # Screenshot output (lihat Bab 8)
│
├── case-02-iot-generator/                      # STUDI KASUS 2
│   ├── main.py                                 # Program utama Case 02
│   ├── README.md                               # Dokumentasi Case 02
│   └── output.png                              # Screenshot output (lihat Bab 8)
│
└── case-03-login-security/                     # STUDI KASUS 3
    ├── main.py                                 # Program utama Case 03
    ├── README.md                               # Dokumentasi Case 03
    └── output.png                              # Screenshot output (lihat Bab 8)
```

---

## 6. Status Pengerjaan
| Task | Status |
|------|--------|
| Struktur folder repository dibuat sesuai soal | ✅ SELESAI |
| Case 01 – Analisis Nilai Mahasiswa | ✅ SELESAI |
| Case 02 – IoT Sensor Generator | ✅ SELESAI |
| Case 03 – Login Security & Audit Log | ✅ SELESAI |
| README per-case (3 buah) | ✅ SELESAI |
| README utama (file ini) | ✅ SELESAI |
| Pengujian eksekusi ketiga program | ✅ DIJALANKAN, TANPA ERROR |
| Validasi matematis & logika | ✅ SESUAI ATURAN SOAL |

---

## 7. Rekomendasi Urutan Commit (Git)
Berikut adalah urutan commit yang direkomendasikan (dapat dijalankan jika repository ini dikelola dengan Git):

```bash
# 1. Inisialisasi repository dan struktur awal
git add .
git commit -m "chore: initialize python advanced case study"

# 2. Selesaikan case 01
git add case-01-analisis-nilai/
git commit -m "feat: implement case 01 student grade analysis"
git commit --allow-empty -m "docs: add case 01 documentation"

# 3. Selesaikan case 02
git add case-02-iot-generator/
git commit -m "feat: implement case 02 iot generator"
git commit --allow-empty -m "docs: add case 02 documentation"

# 4. Selesaikan case 03
git add case-03-login-security/
git commit -m "feat: implement case 03 login security"
git commit --allow-empty -m "docs: add case 03 documentation"

# 5. Pengujian & verifikasi akhir
git add .
git commit -m "test: verify all case executions"

# 6. Update README utama
git add README.md
git commit -m "docs: update main README"
```

> ⚠️ **JANGAN MELAKUKAN `git push`** ke repository online tanpa instruksi eksplisit dari dosen / pemilik repo. Commit hanya lokal saja.

---

## 8. Bukti Screenshot / Output
Setiap folder case menyediakan tempat untuk file `output.png` sebagai bukti eksekusi program.

### 8.1 Lokasi file output
- `case-01-analisis-nilai/output.png` → screenshot terminal setelah menjalankan Case 01.
- `case-02-iot-generator/output.png` → screenshot terminal setelah menjalankan Case 02.
- `case-03-login-security/output.png` → screenshot terminal setelah menjalankan Case 03.

### 8.2 Cara mengambil screenshot (jika environment belum membuatkan)
Karena screenshot membutuhkan visualisasi terminal secara langsung di mesin Anda, lakukan langkah berikut:

1. Jalankan masing-masing program (perintah di Bab 4) sampai selesai.
2. Pastikan output terminal **tampak penuh dan jelas** (jangan terpotong).
3. Gunakan fitur screenshot sistem operasi:
   - **Windows**: Tombol `Win + Shift + S` (pilih region), atau Snipping Tool.
   - **macOS**: `Cmd + Shift + 4` lalu drag area.
   - **Linux**: `PrintScreen` atau aplikasi screenshot default.
4. Pilih seluruh area output terminal program tersebut.
5. Simpan sebagai `output.png` di folder case yang bersangkutan (ganti file jika sudah ada placeholder / kosong).

### 8.3 Output teks tambahan (acuan)
Jika perlu referensi sebelum membuat screenshot, jalankan programnya terlebih dahulu. Semua program memiliki output **berwarna judul, tabel berkolom, dan garis pemisah** sehingga sangat mudah dibaca.

---

## 9. Catatan Tambahan
- Semua kode sengaja ditulis **sederhana, bersih, dan penuh komentar penjelasan** agar mudah dipelajari, dipahami, dan dijelaskan saat presentasi / ditanya dosen.
- **Tidak ada library eksternal yang digunakan** — hanya Python built-in modules (`re`, `datetime`, `random`, `time`).
- Rumus perhitungan di Case 01 sudah divalidasi secara matematis sesuai bobot soal.
- Generator di Case 02 benar-benar menggunakan `yield` (tidak di-backing oleh list besar).
- Decorator di Case 03 benar-benar memisahkan logika logging dari autentikasi.
