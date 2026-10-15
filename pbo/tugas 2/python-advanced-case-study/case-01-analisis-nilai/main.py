"""
STUDI KASUS 1 - ANALISIS NILAI MAHASISWA
Konsep yang digunakan: List Comprehension, Lambda, Filtering, Sorting
"""

# Data awal sesuai soal + 2 mahasiswa tambahan (total 5 mahasiswa)
data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 88, "uts": 82, "uas": 78},
    {"nama": "Elisa", "nim": "230105", "tugas": 75, "uts": 72, "uas": 80},
]

# Bobot penilaian sesuai soal
BOBOT_TUGAS = 0.30  # 30%
BOBOT_UTS = 0.30    # 30%
BOBOT_UAS = 0.40    # 40%


def hitung_nilai_akhir(mhs):
    """Menghitung nilai akhir berdasarkan bobot tugas 30%, UTS 30%, UAS 40%"""
    return (mhs["tugas"] * BOBOT_TUGAS) + (mhs["uts"] * BOBOT_UTS) + (mhs["uas"] * BOBOT_UAS)


def main():
    print("=" * 90)
    print(f"{'PROGRAM ANALISIS NILAI MAHASISWA':^90}")
    print("=" * 90)
    print(f"Bobot: Tugas = 30%  |  UTS = 30%  |  UAS = 40%")
    print()

    # =========================================================================
    # 1. MENGHITUNG NILAI AKHIR SETIAP MAHASISWA (PAKAI LIST COMPREHENSION)
    # =========================================================================
    # List comprehension untuk membuat list baru yang berisi dict mahasiswa
    # ditambah field "nilai_akhir" dan "huruf_mutu"
    print(">" * 90)
    print(" [1] DAFTAR NILAI AKHIR MAHASISWA")
    print(">" * 90)

    daftar_nilai = [
        {
            **mhs,
            "nilai_akhir": round(hitung_nilai_akhir(mhs), 2)
        }
        for mhs in data_mahasiswa
    ]

    # Tampilkan tabel nilai
    print(f"{'NO':<4}{'NAMA':<18}{'NIM':<10}{'TUGAS':<8}{'UTS':<8}{'UAS':<8}{'NILAI AKHIR':<12}")
    print("-" * 90)
    for i, mhs in enumerate(daftar_nilai, start=1):
        print(f"{i:<4}{mhs['nama']:<18}{mhs['nim']:<10}{mhs['tugas']:<8}{mhs['uts']:<8}{mhs['uas']:<8}{mhs['nilai_akhir']:<12.2f}")
    print()

    # =========================================================================
    # 2. MENAMPILKAN MAHASISWA BERPRESTASI (NILAI AKHIR > 80)
    #    Menggunakan filter() + lambda (BUKAN for manual bertingkat)
    # =========================================================================
    print(">" * 90)
    print(" [2] MAHASISWA BERPRESTASI (Nilai Akhir > 80)")
    print(">" * 90)

    # Filtering menggunakan filter() dan lambda function
    mahasiswa_berprestasi = list(
        filter(lambda m: m["nilai_akhir"] > 80, daftar_nilai)
    )

    if mahasiswa_berprestasi:
        print(f"{'NO':<4}{'NAMA':<18}{'NIM':<10}{'NILAI AKHIR':<12}")
        print("-" * 90)
        for i, mhs in enumerate(mahasiswa_berprestasi, start=1):
            print(f"{i:<4}{mhs['nama']:<18}{mhs['nim']:<10}{mhs['nilai_akhir']:<12.2f}")
        print(f"\nTotal mahasiswa berprestasi: {len(mahasiswa_berprestasi)} orang")
    else:
        print("  Tidak ada mahasiswa dengan nilai akhir > 80")
    print()

    # =========================================================================
    # 3. RANKING SELURUH MAHASISWA (TERTINGGI -> TERENDAH)
    #    Menggunakan sorted() dengan key lambda
    # =========================================================================
    print(">" * 90)
    print(" [3] RANKING MAHASISWA BERDASARKAN NILAI AKHIR")
    print(">" * 90)

    ranking = sorted(
        daftar_nilai,
        key=lambda m: m["nilai_akhir"],  # lambda sebagai key sorting
        reverse=True                      # tertinggi ke terendah
    )

    print(f"{'RANK':<6}{'NAMA':<18}{'NIM':<10}{'TUGAS':<8}{'UTS':<8}{'UAS':<8}{'NILAI AKHIR':<12}")
    print("-" * 90)
    for rank, mhs in enumerate(ranking, start=1):
        print(f"{rank:<6}{mhs['nama']:<18}{mhs['nim']:<10}{mhs['tugas']:<8}{mhs['uts']:<8}{mhs['uas']:<8}{mhs['nilai_akhir']:<12.2f}")
    print()

    # =========================================================================
    # 4. MAHASISWA TERBAIK / PERINGKAT PERTAMA
    # =========================================================================
    print(">" * 90)
    print(" [4] MAHASISWA TERBAIK (PERINGKAT 1)")
    print(">" * 90)

    if ranking:
        terbaik = ranking[0]
        print(f"  Nama          : {terbaik['nama']}")
        print(f"  NIM           : {terbaik['nim']}")
        print(f"  Nilai Tugas   : {terbaik['tugas']}")
        print(f"  Nilai UTS     : {terbaik['uts']}")
        print(f"  Nilai UAS     : {terbaik['uas']}")
        print(f"  Nilai Akhir   : {terbaik['nilai_akhir']:.2f}")
        print(f"  Peringkat     : 1 (TERBAIK)")
    print()

    print("=" * 90)
    print(f"{'PROGRAM SELESAI':^90}")
    print("=" * 90)


if __name__ == "__main__":
    main()
