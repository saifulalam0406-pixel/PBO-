# Aplikasi Pengelola Tanggal dan Waktu

Project latihan terminal ini dibuat berdasarkan materi Python `datetime` dan
`time` yang tersedia untuk PBO Sesi #7. Karena instruksi resmi tugas tidak
tersedia, project ini adalah latihan yang sesuai dengan materi, bukan kepastian
mengenai bentuk tugas yang diminta dosen.

## Fitur

- Menampilkan tanggal dan tanggal-waktu saat ini.
- Memformat tanggal dan waktu dengan `strftime()`.
- Membaca teks tanggal-waktu dengan `strptime()` dan menangani input tidak
  valid.
- Mengubah timestamp Unix menjadi tanggal-waktu lokal dengan
  `datetime.fromtimestamp()`. Jika input timestamp dikosongkan, program memakai
  timestamp saat ini dari `time.time()`.
- Menampilkan waktu lokal menggunakan modul `time`.
- Menjalankan hitung mundur 1–10 detik menggunakan `time.sleep()`.

## Cara menjalankan

Pastikan Python 3 terpasang. Dari folder utama project, buka terminal lalu
jalankan:

```bash
python3 sesi-7-datetime-time/main.py
```

Pada Windows, perintahnya dapat berupa:

```bash
py sesi-7-datetime-time/main.py
```

## Format tanggal yang diterima

Untuk menu 3, masukkan tanggal dan waktu dengan pola:

```text
DD-MM-YYYY HH:MM:SS
```

Contoh:

```text
25-12-2026 14:30:00
```

Timestamp pada menu 4 ditafsirkan sebagai waktu lokal komputer, bukan UTC.
Durasi menu hitung mundur dibatasi sampai 10 detik agar jeda tetap singkat.
