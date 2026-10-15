# CASE 02 — STREAMING DATA SENSOR IoT

## 1. Ringkasan Masalah
Dalam sistem IoT (Internet of Things), perangkat sensor biasanya mengirimkan data secara **bertahap dan terus-menerus** (streaming data). Jika semua data disimpan dalam list besar sekaligus, memori akan cepat terbuang sia-sia. Untuk mengatasinya, Python menyediakan fitur **Generator** yang bisa menghasilkan data satu per satu tanpa menampung seluruh data di memori. Studi kasus ini mensimulasikan pembacaan sensor suhu ruangan dari waktu ke waktu.

## 2. Tujuan Program
- Mendemonstrasikan pembuatan **Generator Function** dengan keyword `yield`.
- Menghasilkan data suhu secara bertahap dalam rentang 15.0°C – 38.0°C.
- Membuktikan bahwa **tidak ada list besar** yang menyimpan seluruh data sensor (hemat memori).
- Menunjukkan penggunaan `next()` secara eksplisit dan konsumsi data melalui for-loop.
- Mengkategorikan setiap pembacaan suhu: **Dingin**, **Normal**, atau **Panas**.
- Menampilkan minimal 10 pembacaan suhu berturut-turut di terminal.

## 3. Konsep Python yang Digunakan
| Konsep | Keterangan Penerapan |
|--------|----------------------|
| **Generator Function** | Fungsi `sensor_suhu_generator()` menggunakan `yield` untuk mengeluarkan data satu per satu. |
| **Keyword `yield`** | Mengeluarkan nilai sambil menahan state fungsi agar bisa dilanjutkan kembali (bukan `return` yang mengakhiri fungsi). |
| **Iterator / `next()`** | Konsumsi data generator secara eksplisit satu per satu melalui `next(iterator_1)`. |
| **For-Loop atas Generator** | For-loop secara otomatis memanggil `next()` di belakang layar sampai generator habis. |
| **Lazy Evaluation** | Data baru dihasilkan saat benar-benar diminta (bukan dibuat list di awal). |

## 4. Penjelasan Singkat Cara Kerja Program
1. **Definisi Generator**: `sensor_suhu_generator(jumlah_data, min_suhu, max_suhu, jeda)` adalah generator function. Di dalamnya ada loop `for` dengan `random.uniform()` untuk mensimulasikan pembacaan suhu, lalu `yield nomor, suhu` untuk mengeluarkan data.
2. **Yield Bekerja**: Setiap `yield` tereksekusi, fungsi berhenti sejenak dan mengembalikan satu tuple `(nomor, suhu)`. Ketika pemanggil meminta data berikutnya, fungsi lanjut dari posisi persis setelah yield, bukan dari awal.
3. **Konsumsi Data**:
   - Demo 1: `next()` eksplisit untuk 3 pembacaan pertama → membuktikan konsumsi bertahap.
   - Demo 2: For-loop mengiterasi generator untuk 12 pembacaan → setiap iterasi memicu `next()` otomatis.
4. **Kategorisasi**: `kategorikan_suhu()` membandingkan nilai suhu: `< 20 = Dingin`, `20–30 = Normal`, `> 30 = Panas`.
5. **Demo Konseptual**: Menunjukkan bahwa generator bukan list, tapi objek generator yang *lazy* (hemat memori).

## 5. Struktur / File yang Digunakan
```
case-02-iot-generator/
├── main.py       # Program utama (generator, konsumsi, dan output)
├── README.md     # Dokumentasi ini
└── output.png    # Screenshot output terminal
```

## 6. Cara Menjalankan Program
```bash
cd case-02-iot-generator
python main.py
```
Atau dari root project:
```bash
python case-02-iot-generator/main.py
```

## 7. Contoh Output (Ringkasan)
```
================================================================================
               PROGRAM STREAMING DATA SENSOR IoT (SUHU RUANGAN)
================================================================================
Rentang suhu simulasi  : 15.0°C - 38.0°C
Kategori suhu          : <20 Dingin | 20-30 Normal | >30 Panas
Total pembacaan        : 12 data

[DEMO 1] KONSUMSI DENGAN next() SECARA EKSPLISIT (3 data pertama)
NO    SUHU (°C)     KATEGORI    KETERANGAN
--------------------------------------------------------------------------------
1     17.2          Dingin      ❄️
2     25.8          Normal      ✅
3     33.4          Panas       🔥

[DEMO 2] STREAMING 12 DATA SENSOR BERTAHAP (for-loop + generator)
  -> Setiap data dihasilkan saat iterasi (TIDAK ada list besar di memori)
NO    SUHU (°C)     KATEGORI    KETERANGAN
--------------------------------------------------------------------------------
1     22.1          Normal      ✅
2     18.9          Dingin      ❄️
...
12    35.2          Panas       🔥
--------------------------------------------------------------------------------
Rata-rata suhu  : 26.1°C
Suhu tertinggi  : 37.1°C
Suhu terendah   : 16.3°C
Total pembacaan : 12 data

[DEMO 3] BUKTI KONSEPTUAL GENERATOR
Tipe generator_contoh : generator
Apakah ini list?       : False
Sifatnya lazy          : Data baru dihasilkan ketika next() dipanggil
Memori terpakai        : Hanya state generator, bukan list besar data.
```

## 8. Penjelasan Requirement yang Sudah Dipenuhi
| Requirement Soal | Status |
|------------------|--------|
| **Generator Function** pakai `yield` | ✅ `sensor_suhu_generator()` memakai `yield` bukan list |
| Hasilkan data suhu bertahap 15–38°C | ✅ `random.uniform(15.0, 38.0)` |
| Tidak buat list besar dulu | ✅ Tidak ada `[suhu for ... in range(jumlah)]`; data dibuat 1 per 1 |
| Data dikonsumsi satu per satu | ✅ Demo 1 pakai `next()` eksplisit |
| Demonstrasi iterator / generator | ✅ `iter(generator_1)` + `next()` |
| Kategori suhu: Dingin/Normal/Panas | ✅ Fungsi `kategorikan_suhu()` dengan aturan <20 / 20–30 / >30 |
| Minimal 10 pembacaan ditampilkan | ✅ Demo 2 menampilkan 12 pembacaan |
| Output rapi mudah dibaca | ✅ Tabel berkolom, simbol, statistik ringkas |
| Komentar penjelasan generator/yield | ✅ Ada kotak penjelasan di awal kode + per baris kritis |
| Buktikan pendekatan hemat memori | ✅ Demo 3 menunjukkan tipe objek generator (bukan list), sifat lazy |
