# ============================================================
# SISTEM PERPUSTAKAAN BERBASIS OOP - PYTHON
# ============================================================
# Berisi 6 Class: Buku, Anggota, Pustakawan, RakBuku, Peminjaman, Perpustakaan
# Setiap Class memiliki minimal 2 Attribute & minimal 1 Method
# ============================================================

from datetime import datetime, timedelta

# ============================================================
# CLASS 1: BUKU
# ============================================================
# Penjelasan Class:
# Class Buku merepresentasikan sebuah buku fisik yang ada di perpustakaan.
# Objek dari class ini akan menyimpan informasi detail buku.
#
# Attribute:
# - isbn (str)        : Nomor ISBN unik untuk identifikasi buku
# - judul (str)       : Judul buku
# - penulis (str)     : Nama penulis buku
# - tahun_terbit (int): Tahun terbit buku
# - tersedia (bool)   : Status ketersediaan buku (True = bisa dipinjam)
#
# Method:
# - pinjam()     : Mengubah status ketersediaan menjadi False
# - kembalikan() : Mengubah status ketersediaan menjadi True
# - info_buku()  : Menampilkan informasi lengkap buku
# ============================================================
class Buku:
    def __init__(self, isbn, judul, penulis, tahun_terbit):
        self.isbn = isbn
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.tersedia = True

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def kembalikan(self):
        self.tersedia = True

    def info_buku(self):
        status = "Tersedia" if self.tersedia else "Sedang Dipinjam"
        return (f"ISBN: {self.isbn} | Judul: {self.judul} | "
                f"Penulis: {self.penulis} | Tahun: {self.tahun_terbit} | "
                f"Status: {status}")


# ============================================================
# CLASS 2: ANGGOTA
# ============================================================
# Penjelasan Class:
# Class Anggota merepresentasikan anggota perpustakaan yang berhak
# meminjam dan mengembalikan buku.
#
# Attribute:
# - id_anggota (str)   : ID unik anggota perpustakaan
# - nama (str)         : Nama lengkap anggota
# - jurusan (str)      : Jurusan / bidang anggota
# - denda (float)      : Jumlah denda yang harus dibayar
# - riwayat (list)     : Daftar riwayat peminjaman buku
#
# Method:
# - tambah_denda(jumlah)  : Menambahkan nominal denda anggota
# - bayar_denda(jumlah)   : Membayar denda (mengurangi nominal denda)
# - cetak_riwayat()       : Menampilkan semua riwayat peminjaman
# ============================================================
class Anggota:
    def __init__(self, id_anggota, nama, jurusan):
        self.id_anggota = id_anggota
        self.nama = nama
        self.jurusan = jurusan
        self.denda = 0.0
        self.riwayat = []

    def tambah_denda(self, jumlah):
        self.denda += jumlah
        return f"Denda ditambahkan Rp{jumlah:,}. Total denda sekarang: Rp{self.denda:,}"

    def bayar_denda(self, jumlah):
        if jumlah <= self.denda:
            self.denda -= jumlah
            return f"Pembayaran berhasil. Sisa denda: Rp{self.denda:,}"
        return f"Jumlah pembayaran melebihi denda. Denda hanya Rp{self.denda:,}"

    def cetak_riwayat(self):
        if not self.riwayat:
            return "Belum ada riwayat peminjaman."
        hasil = [f"Riwayat Peminjaman {self.nama}:"]
        for i, item in enumerate(self.riwayat, 1):
            hasil.append(f"  {i}. {item}")
        return "\n".join(hasil)


# ============================================================
# CLASS 3: PUSTAKAWAN
# ============================================================
# Penjelasan Class:
# Class Pustakawan merepresentasikan staf / pegawai perpustakaan
# yang bertugas mengelola operasional perpustakaan.
#
# Attribute:
# - nip (str)           : Nomor Induk Pegawai
# - nama (str)          : Nama lengkap pustakawan
# - shift (str)         : Shift kerja (Pagi / Siang / Sore)
# - tugas (list)        : Daftar tugas yang dikerjakan hari ini
#
# Method:
# - tambah_tugas(tugas) : Menambahkan tugas baru ke daftar
# - selesaikan_tugas()  : Menghapus tugas paling atas dari daftar
# - info_pustakawan()   : Menampilkan informasi pustakawan & tugas
# ============================================================
class Pustakawan:
    def __init__(self, nip, nama, shift):
        self.nip = nip
        self.nama = nama
        self.shift = shift
        self.tugas = []

    def tambah_tugas(self, tugas):
        self.tugas.append(tugas)
        return f"Tugas '{tugas}' ditambahkan ke daftar {self.nama}."

    def selesaikan_tugas(self):
        if self.tugas:
            selesai = self.tugas.pop(0)
            return f"Tugas '{selesai}' telah diselesaikan."
        return "Tidak ada tugas yang harus diselesaikan."

    def info_pustakawan(self):
        info = [f"NIP: {self.nip} | Nama: {self.nama} | Shift: {self.shift}"]
        if self.tugas:
            info.append("Daftar Tugas:")
            for i, t in enumerate(self.tugas, 1):
                info.append(f"  {i}. {t}")
        else:
            info.append("Tidak ada tugas aktif.")
        return "\n".join(info)


# ============================================================
# CLASS 4: RAKBUKU
# ============================================================
# Penjelasan Class:
# Class RakBuku merepresentasikan rak penyimpanan fisik buku
# di dalam perpustakaan yang dikelompokkan berdasarkan kategori.
#
# Attribute:
# - kode_rak (str)    : Kode unik rak (misal: FIK-01, SAINS-02)
# - kategori (str)    : Kategori buku pada rak (Fiksi, Sains, dll)
# - kapasitas (int)   : Kapasitas maksimal rak
# - daftar_buku (list): Daftar objek Buku yang ada di rak
#
# Method:
# - tambah_buku(buku)  : Menambahkan buku ke dalam rak
# - hapus_buku(isbn)   : Menghapus buku dari rak berdasarkan ISBN
# - cari_buku(judul)   : Mencari buku berdasarkan judul
# ============================================================
class RakBuku:
    def __init__(self, kode_rak, kategori, kapasitas):
        self.kode_rak = kode_rak
        self.kategori = kategori
        self.kapasitas = kapasitas
        self.daftar_buku = []

    def tambah_buku(self, buku):
        if len(self.daftar_buku) < self.kapasitas:
            self.daftar_buku.append(buku)
            return f"Buku '{buku.judul}' berhasil ditambahkan ke Rak {self.kode_rak}."
        return f"Rak {self.kode_rak} sudah penuh! Tidak bisa menambah buku."

    def hapus_buku(self, isbn):
        for buku in self.daftar_buku:
            if buku.isbn == isbn:
                self.daftar_buku.remove(buku)
                return f"Buku dengan ISBN {isbn} dihapus dari Rak {self.kode_rak}."
        return f"Buku dengan ISBN {isbn} tidak ditemukan di Rak {self.kode_rak}."

    def cari_buku(self, judul):
        hasil = [b for b in self.daftar_buku if judul.lower() in b.judul.lower()]
        if hasil:
            return [b.info_buku() for b in hasil]
        return [f"Buku dengan judul '{judul}' tidak ditemukan di Rak {self.kode_rak}."]


# ============================================================
# CLASS 5: PEMINJAMAN
# ============================================================
# Penjelasan Class:
# Class Peminjaman merepresentasikan transaksi peminjaman buku
# antara anggota perpustakaan dengan buku yang dipinjam.
#
# Attribute:
# - id_pinjam (str)    : ID unik transaksi peminjaman
# - anggota (Anggota)  : Objek Anggota yang meminjam
# - buku (Buku)        : Objek Buku yang dipinjam
# - tanggal_pinjam (dt): Tanggal mulai peminjaman
# - tanggal_kembali (dt): Tanggal pengembalian (7 hari setelah pinjam)
# - dikembalikan (bool): Status apakah sudah dikembalikan
#
# Method:
# - proses_peminjaman() : Menjalankan proses pinjam buku
# - proses_pengembalian(): Menjalankan proses pengembalian buku
# - hitung_denda()      : Menghitung denda jika terlambat mengembalikan
# ============================================================
class Peminjaman:
    def __init__(self, id_pinjam, anggota, buku):
        self.id_pinjam = id_pinjam
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = datetime.now()
        self.tanggal_kembali = self.tanggal_pinjam + timedelta(days=7)
        self.dikembalikan = False

    def proses_peminjaman(self):
        if self.buku.pinjam():
            riwayat = f"Pinjam: {self.buku.judul} | {self.tanggal_pinjam.strftime('%d-%m-%Y')}"
            self.anggota.riwayat.append(riwayat)
            return (f"Peminjaman berhasil!\nID Pinjam: {self.id_pinjam}\n"
                    f"Peminjam: {self.anggota.nama}\nBuku: {self.buku.judul}\n"
                    f"Tanggal Kembali: {self.tanggal_kembali.strftime('%d-%m-%Y')}")
        return f"Peminjaman gagal! Buku '{self.buku.judul}' sedang tidak tersedia."

    def proses_pengembalian(self):
        if not self.dikembalikan:
            self.dikembalikan = True
            self.buku.kembalikan()
            denda = self.hitung_denda()
            if denda > 0:
                self.anggota.tambah_denda(denda)
                return (f"Pengembalian berhasil! Terlambat {self._hitung_keterlambatan()} hari.\n"
                        f"Denda keterlambatan: Rp{denda:,}")
            return f"Pengembalian berhasil! Tidak ada denda."
        return "Buku ini sudah dikembalikan sebelumnya."

    def _hitung_keterlambatan(self):
        sekarang = datetime.now()
        if sekarang > self.tanggal_kembali:
            return (sekarang - self.tanggal_kembali).days
        return 0

    def hitung_denda(self):
        terlambat = self._hitung_keterlambatan()
        tarif_per_hari = 2000
        return terlambat * tarif_per_hari


# ============================================================
# CLASS 6: PERPUSTAKAAN
# ============================================================
# Penjelasan Class:
# Class Perpustakaan adalah class utama yang mengagregasi semua elemen
# sistem perpustakaan (buku, anggota, pustakawan, rak, peminjaman).
#
# Attribute:
# - nama (str)           : Nama perpustakaan
# - alamat (str)         : Alamat perpustakaan
# - daftar_anggota (list): Semua anggota yang terdaftar
# - daftar_pustakawan (list): Semua pustakawan yang bekerja
# - daftar_rak (list)    : Semua rak buku di perpustakaan
# - daftar_peminjaman (list): Semua transaksi peminjaman
#
# Method:
# - daftar_anggota_baru(anggota)  : Mendaftarkan anggota baru
# - tambah_rak(rak)               : Menambahkan rak baru
# - laporan_stok_buku()           : Membuat laporan semua stok buku
# - laporan_peminjaman_aktif()    : Membuat laporan peminjaman aktif
# ============================================================
class Perpustakaan:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.daftar_anggota = []
        self.daftar_pustakawan = []
        self.daftar_rak = []
        self.daftar_peminjaman = []

    def daftar_anggota_baru(self, anggota):
        self.daftar_anggota.append(anggota)
        return f"Anggota {anggota.nama} (ID: {anggota.id_anggota}) berhasil didaftarkan."

    def tambah_rak(self, rak):
        self.daftar_rak.append(rak)
        return f"Rak {rak.kode_rak} - {rak.kategori} ditambahkan ke {self.nama}."

    def laporan_stok_buku(self):
        laporan = [f"=== LAPORAN STOK BUKU {self.nama.upper()} ===",
                   f"Alamat: {self.alamat}", ""]
        total_buku = 0
        for rak in self.daftar_rak:
            laporan.append(f"Rak {rak.kode_rak} ({rak.kategori}):")
            for buku in rak.daftar_buku:
                laporan.append(f"  - {buku.info_buku()}")
                total_buku += 1
            if not rak.daftar_buku:
                laporan.append("  (Rak kosong)")
            laporan.append("")
        laporan.append(f"Total Buku Keseluruhan: {total_buku} buku")
        return "\n".join(laporan)

    def laporan_peminjaman_aktif(self):
        laporan = [f"=== LAPORAN PEMINJAMAN AKTIF ===", ""]
        aktif = [p for p in self.daftar_peminjaman if not p.dikembalikan]
        if not aktif:
            laporan.append("Tidak ada peminjaman aktif saat ini.")
        else:
            for p in aktif:
                laporan.append(f"ID: {p.id_pinjam} | {p.anggota.nama} -> {p.buku.judul}")
                laporan.append(f"   Kembali: {p.tanggal_kembali.strftime('%d-%m-%Y')}")
        return "\n".join(laporan)


# ============================================================
# CONTOH PEMANGGILAN / INSTANSIASI OBJECT
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("DEMO SISTEM PERPUSTAKAAN BERBASIS OOP")
    print("=" * 70)

    # --- INSTANSIASI CLASS PERPUSTAKAAN ---
    print("\n>>> 1. MEMBUAT OBJEK PERPUSTAKAAN")
    perpus = Perpustakaan("Perpustakaan Universitas Cerdas", "Jl. Ilmu No. 123, Kota Pintar")
    print(f"Perpustakaan '{perpus.nama}' di {perpus.alamat} siap beroperasi!")

    # --- INSTANSIASI CLASS PUSTAKAWAN ---
    print("\n>>> 2. MEMBUAT OBJEK PUSTAKAWAN")
    pustakawan1 = Pustakawan("PK-001", "Siti Rahmawati", "Pagi")
    pustakawan2 = Pustakawan("PK-002", "Budi Santoso", "Siang")
    perpus.daftar_pustakawan.extend([pustakawan1, pustakawan2])
    print(pustakawan1.info_pustakawan())
    print("-" * 50)
    print(pustakawan2.tambah_tugas("Merapikan rak Fiksi"))
    print(pustakawan2.tambah_tugas("Membantu anggota mencari buku"))
    print(pustakawan2.info_pustakawan())
    print(pustakawan2.selesaikan_tugas())
    print(pustakawan2.info_pustakawan())

    # --- INSTANSIASI CLASS RAKBUKU ---
    print("\n>>> 3. MEMBUAT OBJEK RAK BUKU")
    rak_fiksi = RakBuku("RAK-F-01", "Fiksi", 50)
    rak_sains = RakBuku("RAK-S-01", "Sains & Teknologi", 40)
    perpus.tambah_rak(rak_fiksi)
    perpus.tambah_rak(rak_sains)
    print(f"Rak {rak_fiksi.kode_rak} (Kapasitas: {rak_fiksi.kapasitas}) dibuat!")
    print(f"Rak {rak_sains.kode_rak} (Kapasitas: {rak_sains.kapasitas}) dibuat!")

    # --- INSTANSIASI CLASS BUKU ---
    print("\n>>> 4. MEMBUAT OBJEK BUKU & MEMASUKKAN KE RAK")
    buku1 = Buku("978-602-8519-93-4", "Laskar Pelangi", "Andrea Hirata", 2005)
    buku2 = Buku("978-979-1227-00-7", "Bumi Manusia", "Pramoedya Ananta Toer", 1980)
    buku3 = Buku("978-0-13-468599-1", "Python Crash Course", "Eric Matthes", 2019)
    buku4 = Buku("978-1-4919-4600-8", "Fluent Python", "Luciano Ramalho", 2015)

    print(rak_fiksi.tambah_buku(buku1))
    print(rak_fiksi.tambah_buku(buku2))
    print(rak_sains.tambah_buku(buku3))
    print(rak_sains.tambah_buku(buku4))

    print("\nHasil pencarian buku 'Python':")
    for hasil in rak_sains.cari_buku("Python"):
        print(f"  {hasil}")

    # --- INSTANSIASI CLASS ANGGOTA ---
    print("\n>>> 5. MEMBUAT OBJEK ANGGOTA PERPUSTAKAAN")
    anggota1 = Anggota("AG-1001", "Dewi Lestari", "Teknik Informatika")
    anggota2 = Anggota("AG-1002", "Ahmad Rizki", "Sistem Informasi")
    perpus.daftar_anggota_baru(anggota1)
    perpus.daftar_anggota_baru(anggota2)
    print(f"Anggota: {anggota1.nama} | {anggota1.id_anggota} | {anggota1.jurusan}")
    print(f"Anggota: {anggota2.nama} | {anggota2.id_anggota} | {anggota2.jurusan}")

    # --- INSTANSIASI CLASS PEMINJAMAN ---
    print("\n>>> 6. MEMBUAT TRANSAKSI PEMINJAMAN BUKU")
    pinjam1 = Peminjaman("TRX-001", anggota1, buku1)
    pinjam2 = Peminjaman("TRX-002", anggota2, buku3)
    perpus.daftar_peminjaman.extend([pinjam1, pinjam2])

    print(pinjam1.proses_peminjaman())
    print("-" * 50)
    print(pinjam2.proses_peminjaman())
    print("-" * 50)

    print("\n>>> Status Buku Setelah Dipinjam:")
    print(f"  {buku1.info_buku()}")
    print(f"  {buku3.info_buku()}")

    # --- PROSES PENGEMBALIAN ---
    print("\n>>> 7. PROSES PENGEMBALIAN BUKU")
    print(pinjam1.proses_pengembalian())
    print("\nStatus Buku Setelah Dikembalikan:")
    print(f"  {buku1.info_buku()}")

    # --- RIWAYAT ANGGOTA ---
    print("\n>>> 8. RIWAYAT DAN DENDA ANGGOTA")
    print(anggota1.cetak_riwayat())
    print("-" * 50)
    print(anggota1.tambah_denda(5000))
    print(anggota1.bayar_denda(3000))
    print(f"Sisa denda {anggota1.nama}: Rp{anggota1.denda:,}")

    # --- LAPORAN PERPUSTAKAAN ---
    print("\n>>> 9. LAPORAN AKHIR PERPUSTAKAAN")
    print(perpus.laporan_stok_buku())
    print("\n")
    print(perpus.laporan_peminjaman_aktif())

    print("\n" + "=" * 70)
    print("SELESAI! Semua Class berhasil diinstansiasi dan dijalankan.")
    print("=" * 70)
