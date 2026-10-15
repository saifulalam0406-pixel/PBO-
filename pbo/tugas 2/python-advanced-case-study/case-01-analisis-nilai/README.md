# CASE 01 — ANALISIS NILAI MAHASISWA

## 1. Ringkasan Masalah
Program ini bertujuan menganalisis data nilai mahasiswa secara otomatis, mulai dari menghitung nilai akhir dengan bobot tertentu, menyaring mahasiswa berprestasi, hingga membuat peringkat berdasarkan nilai akhir tertinggi. Data mahasiswa disimpan dalam bentuk list of dictionaries yang memuat nama, NIM, nilai tugas, UTS, dan UAS.

## 2. Tujuan Program
- Menghitung nilai akhir setiap mahasiswa berdasarkan bobot: Tugas 30%, UTS 30%, UAS 40%.
- Menyaring dan menampilkan mahasiswa berprestasi dengan nilai akhir di atas 80.
- Membuat ranking mahasiswa dari nilai tertinggi sampai terendah.
- Menampilkan mahasiswa terbaik (peringkat 1) beserta detail nilainya.
- Membuktikan penggunaan konsep Python tingkat lanjut: List Comprehension, Lambda, Filtering, dan Sorting.

## 3. Konsep Python yang Digunakan
| Konsep | Keterangan Penerapan |
|--------|----------------------|
| **List Comprehension** | Digunakan untuk membangun list `daftar_nilai` (transformasi data mahasiswa + tambah field `nilai_akhir`) dengan sintaks ringkas, tanpa for-loop append manual bertumpuk. |
| **Lambda Function** | (1) Sebagai argumen `key` di `filter()` untuk kriteria nilai > 80. (2) Sebagai argumen `key` di `sorted()` untuk sorting berdasarkan `nilai_akhir`. |
| **Filtering (filter())** | Menyaring mahasiswa berprestasi (nilai_akhir > 80) tanpa for manual bertingkat, sesuai aturan soal. |
| **Sorting (sorted())** | Membuat ranking tertinggi → terendah dengan `reverse=True` dan `key=lambda`. |
| **Dictionary** | Menyimpan record data mahasiswa (nama, NIM, tugas, UTS, UAS, nilai_akhir). |

## 4. Penjelasan Singkat Cara Kerja Program
1. **Data Awal**: Terdapat 3 mahasiswa sesuai soal + 2 mahasiswa tambahan (Dimas dan Elisa), total 5 mahasiswa.
2. **Kalkulasi Nilai Akhir**: Fungsi `hitung_nilai_akhir()` mengembalikan rumus `tugas*0.30 + uts*0.30 + uas*0.40`. Dilewatkan ke dalam List Comprehension untuk membangun list baru bernama `daftar_nilai`.
3. **Filter Prestasi**: `filter(lambda m: m["nilai_akhir"] > 80, daftar_nilai)` menghasilkan iterator yang dikonversi menjadi list mahasiswa berprestasi.
4. **Ranking**: `sorted(daftar_nilai, key=lambda m: m["nilai_akhir"], reverse=True)` menghasilkan list ranking.
5. **Mahasiswa Terbaik**: Elemen indeks-0 dari ranking adalah mahasiswa terbaik.
6. **Output**: Semua hasil dicetak ke terminal dalam bentuk tabel agar mudah dibaca.

## 5. Struktur / File yang Digunakan
```
case-01-analisis-nilai/
├── main.py       # Program utama (satu file, tanpa library eksternal)
├── README.md     # Dokumentasi ini
└── output.png    # Screenshot output terminal (dihasilkan manual setelah run)
```

## 6. Cara Menjalankan Program
Pastikan Python 3 terpasang di komputer. Buka terminal, masuk ke folder ini, lalu jalankan:
```bash
cd case-01-analisis-nilai
python main.py
```
Atau dari root project:
```bash
python case-01-analisis-nilai/main.py
```

## 7. Contoh Output (Ringkasan)
```
==========================================================================================
                          PROGRAM ANALISIS NILAI MAHASISWA
==========================================================================================
Bobot: Tugas = 30%  |  UTS = 30%  |  UAS = 40%

NO  NAMA              NIM       TUGAS   UTS     UAS     NILAI AKHIR
------------------------------------------------------------------------------------------
1   Aisyah            230101    85      80      88      84.70
...

[2] MAHASISWA BERPRESTASI (Nilai Akhir > 80)
Aisyah, Cantika, Dimas

[3] RANKING
1. Cantika (90.10)
2. Aisyah (84.70)
3. Dimas ...

[4] MAHASISWA TERBAIK
  Nama          : Cantika
  NIM           : 230103
  Nilai Akhir   : 90.10
  Peringkat     : 1 (TERBAIK)
```

## 8. Penjelasan Requirement yang Sudah Dipenuhi
| Requirement Soal | Status |
|------------------|--------|
| Data awal 3 mahasiswa soal + min 2 tambahan | ✅ Total 5 mahasiswa (Aisyah, Budi, Cantika, Dimas, Elisa) |
| Bobot Tugas 30% / UTS 30% / UAS 40% | ✅ Rumus di `hitung_nilai_akhir()` |
| Hitung nilai akhir setiap mahasiswa | ✅ Ditampilkan dalam tabel |
| **List Comprehension** untuk kalkulasi/transformasi | ✅ Pembuatan `daftar_nilai` |
| Mahasiswa berprestasi nilai > 80 | ✅ Sesi [2] dengan filter + lambda |
| Tanpa for manual bertingkat untuk filter | ✅ Pakai `filter()` bawaan |
| Ranking tertinggi → terendah | ✅ Sesi [3] dengan `sorted()` |
| `sorted()` dengan **key lambda** | ✅ `key=lambda m: m["nilai_akhir"]` |
| **Lambda function** sesuai requirement | ✅ Dipakai di filter dan sorted |
| Mahasiswa terbaik (peringkat 1) | ✅ Sesi [4] |
| Tampilkan nama, NIM, tugas, UTS, UAS, nilai akhir, ranking | ✅ Semua field muncul di tabel ranking |
| Output terminal rapi | ✅ Tabel berkolom, garis pemisah, judul jelas |
| Perhitungan matematis benar | ✅ Rumus sesuai bobot, hasil konsisten |
