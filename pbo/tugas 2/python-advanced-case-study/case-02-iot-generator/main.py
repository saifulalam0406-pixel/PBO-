"""
STUDI KASUS 2 - STREAMING DATA SENSOR IoT
Konsep yang digunakan: Generator Function, yield, Iterator, Konsumsi Data Bertahap
"""

import random
import time


# =============================================================================
# PENJELASAN SINGKAT KONSEP GENERATOR:
# -----------------------------------------------------------------------------
# 1. Apa itu Generator?
#    Generator adalah fungsi khusus di Python yang menghasilkan serangkaian
#    nilai SECARA BERTAHAP, bukan sekaligus. Ciri-cirinya menggunakan keyword
#    YIELD di dalamnya, bukan RETURN.
#
# 2. Bagaimana yield bekerja?
#    Setiap kali yield dieksekusi, fungsi akan:
#      - Mengeluarkan (yield) satu nilai ke pemanggil
#      - MENGHENTIKAN SEMENTARA eksekusi (state-nya disimpan)
#      - Dilanjutkan lagi dari posisi yang sama ketika next() dipanggil lagi
#
# 3. Mengapa lebih hemat memori?
#    Generator TIDAK menyimpan SELURUH data dalam list besar di memori.
#    Hanya SATU data yang dibuat dan dikonsumsi pada satu waktu. Ini sangat
#    berguna untuk data streaming seperti sensor IoT yang bisa tak terbatas.
# =============================================================================


def sensor_suhu_generator(jumlah_data=15, min_suhu=15.0, max_suhu=38.0, jeda=False):
    """
    GENERATOR FUNCTION yang menghasilkan data suhu secara bertahap.
    PENTING: Data dihasilkan SATU PER SATU dengan YIELD, bukan dibuat list dulu!

    Parameter:
        jumlah_data : banyaknya pembacaan yang akan dihasilkan
        min_suhu    : batas bawah suhu (°C)
        max_suhu    : batas atas suhu (°C)
        jeda        : jika True, ada delay 0.3s tiap pembacaan (simulasi real-time)
    """
    for nomor in range(1, jumlah_data + 1):
        # Simulasikan pembacaan sensor saat ini (bukan dari list yang disimpan dulu)
        suhu = round(random.uniform(min_suhu, max_suhu), 1)

        # =====================================================================
        # YIELD = mengeluarkan 1 data dan menunda eksekusi sampai next() dipanggil
        # Ini inti dari generator. Nilai dihasilkan TIDAK disimpan semuanya dulu.
        # =====================================================================
        yield nomor, suhu

        # Simulasi jeda pembacaan sensor (opsional)
        if jeda:
            time.sleep(0.3)


def kategorikan_suhu(suhu):
    """Mengkategorikan suhu berdasarkan rentang yang ditentukan soal."""
    if suhu < 20:
        return "Dingin", "[Dingin]"
    elif 20 <= suhu <= 30:
        return "Normal", "[Normal]"
    else:  # suhu > 30
        return "Panas", "[Panas]"


def main():
    print("=" * 80)
    print(f"{'PROGRAM STREAMING DATA SENSOR IoT (SUHU RUANGAN)':^80}")
    print("=" * 80)
    print(f"Rentang suhu simulasi  : 15.0°C - 38.0°C")
    print(f"Kategori suhu          : <20 Dingin | 20-30 Normal | >30 Panas")
    print(f"Total pembacaan        : 12 data (minimal 10 sesuai requirement)")
    print("-" * 80)
    print()

    # =========================================================================
    # DEMO 1: Menggunakan next() secara eksplisit untuk 3 pembacaan pertama
    # Ini menunjukkan KONSUMSI BERTAPAH yang sebenarnya dari generator.
    # =========================================================================
    print(">" * 80)
    print(" [DEMO 1] KONSUMSI DENGAN next() SECARA EKSPLISIT (3 data pertama)")
    print(">" * 80)
    print(f"{'NO':<6}{'SUHU (°C)':<14}{'KATEGORI':<12}{'KETERANGAN'}")
    print("-" * 80)

    # Buat instance generator
    generator_1 = sensor_suhu_generator(jumlah_data=3, jeda=False)
    iterator_1 = iter(generator_1)  # Dapatkan iterator dari generator

    try:
        for _ in range(3):
            nomor, suhu = next(iterator_1)  # Ambil 1 data secara eksplisit
            kategori, simbol = kategorikan_suhu(suhu)
            print(f"{nomor:<6}{suhu:<14.1f}{kategori:<12}{simbol}")
    except StopIteration:
        pass
    print()

    # =========================================================================
    # DEMO 2: Menggunakan for-loop (for-loop otomatis memanggil next() di belakang)
    # Menampilkan minimal 10 pembacaan sesuai requirement.
    # Setiap data dihasilkan TIDAK dari list besar, melainkan saat iterasi berjalan.
    # =========================================================================
    print(">" * 80)
    print(" [DEMO 2] STREAMING 12 DATA SENSOR BERTAHAP (for-loop + generator)")
    print("  -> Setiap data dihasilkan saat iterasi (TIDAK ada list besar di memori)")
    print(">" * 80)
    print(f"{'NO':<6}{'SUHU (°C)':<14}{'KATEGORI':<12}{'KETERANGAN'}")
    print("-" * 80)

    total_pembacaan = 0
    suhu_total = 0.0
    tertinggi = None
    terendah = None

    # Generator dipakai di sini. Yield dieksekusi setiap iterasi for.
    for nomor, suhu in sensor_suhu_generator(jumlah_data=12, jeda=False):
        kategori, simbol = kategorikan_suhu(suhu)
        print(f"{nomor:<6}{suhu:<14.1f}{kategori:<12}{simbol}")

        # Statistik sederhana (satu per satu, tanpa list)
        total_pembacaan += 1
        suhu_total += suhu
        tertinggi = suhu if tertinggi is None or suhu > tertinggi else tertinggi
        terendah = suhu if terendah is None or suhu < terendah else terendah

    print("-" * 80)
    if total_pembacaan > 0:
        rata_rata = suhu_total / total_pembacaan
        print(f"Rata-rata suhu  : {rata_rata:.1f}°C")
        print(f"Suhu tertinggi  : {tertinggi:.1f}°C")
        print(f"Suhu terendah   : {terendah:.1f}°C")
        print(f"Total pembacaan : {total_pembacaan} data")
    print()

    # =========================================================================
    # DEMO 3: BUKTI bahwa generator TIDAK menyimpan data (list kosong jika cek)
    # =========================================================================
    print(">" * 80)
    print(" [DEMO 3] BUKTI KONSEPTUAL GENERATOR")
    print(">" * 80)
    gen_contoh = sensor_suhu_generator(jumlah_data=5)
    print(f"Tipe generator_contoh : {type(gen_contoh).__name__}")
    print(f"Apakah ini list?       : {isinstance(gen_contoh, list)}")
    print(f"Sifatnya lazy          : Data baru dihasilkan ketika next() dipanggil")
    print(f"Memori terpakai        : Hanya state generator, bukan list besar data.")
    print()

    print("=" * 80)
    print(f"{'PROGRAM SELESAI':^80}")
    print("=" * 80)


if __name__ == "__main__":
    main()
