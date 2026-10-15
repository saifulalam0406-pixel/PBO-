from datetime import date, datetime
import time


class AplikasiPengelolaWaktu:
    """Menu latihan sederhana untuk mengelola tanggal dan waktu."""

    FORMAT_INPUT = "%d-%m-%Y %H:%M:%S"

    def jalankan(self):
        while True:
            print("\n=== APLIKASI PENGELOLA TANGGAL DAN WAKTU ===")
            print("1. Tampilkan tanggal dan waktu sekarang")
            print("2. Tampilkan beberapa format tanggal (strftime)")
            print("3. Ubah teks menjadi tanggal-waktu (strptime)")
            print("4. Ubah timestamp menjadi tanggal-waktu")
            print("5. Tampilkan waktu sekarang (modul time)")
            print("6. Jalankan hitung mundur (time.sleep)")
            print("0. Keluar")

            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                self.tampilkan_tanggal_dan_waktu()
            elif pilihan == "2":
                self.tampilkan_format_tanggal()
            elif pilihan == "3":
                self.parse_tanggal()
            elif pilihan == "4":
                self.konversi_timestamp()
            elif pilihan == "5":
                self.tampilkan_waktu()
            elif pilihan == "6":
                self.jalankan_timer()
            elif pilihan == "0":
                print("Program selesai. Terima kasih sudah belajar!")
                break
            else:
                print("Pilihan tidak tersedia. Masukkan angka 0 sampai 6.")

    @staticmethod
    def tampilkan_tanggal_dan_waktu():
        sekarang = datetime.now()
        hari_ini = date.today()

        print(f"Tanggal hari ini : {hari_ini.strftime('%d-%m-%Y')}")
        print(f"Tanggal & waktu : {sekarang.strftime('%d-%m-%Y %H:%M:%S')}")

    @staticmethod
    def tampilkan_format_tanggal():
        sekarang = datetime.now()

        print("Tanggal angka   :", sekarang.strftime("%d-%m-%Y"))
        print("Tanggal lengkap :", sekarang.strftime("%A, %d %B %Y"))
        print("Jam             :", sekarang.strftime("%H:%M:%S"))

    def parse_tanggal(self):
        teks_tanggal = input(
            "Masukkan tanggal-waktu (DD-MM-YYYY HH:MM:SS): "
        ).strip()

        try:
            hasil_parse = datetime.strptime(teks_tanggal, self.FORMAT_INPUT)
        except ValueError:
            print(
                "Tanggal atau format tidak valid. "
                "Contoh yang benar: 25-12-2026 14:30:00"
            )
            return

        print("Berhasil dibaca sebagai objek datetime.")
        print("Hasil standar:", hasil_parse.strftime("%Y-%m-%d %H:%M:%S"))

    @staticmethod
    def konversi_timestamp():
        teks_timestamp = input(
            "Masukkan timestamp Unix (kosongkan untuk waktu sekarang): "
        ).strip()

        if teks_timestamp:
            try:
                timestamp = float(teks_timestamp)
            except ValueError:
                print("Timestamp harus berupa angka, misalnya 1792134000.")
                return
        else:
            timestamp = time.time()

        try:
            hasil_konversi = datetime.fromtimestamp(timestamp)
        except (OverflowError, OSError, ValueError):
            print("Timestamp berada di luar rentang tanggal yang dapat dibaca.")
            return

        print(f"Timestamp Unix : {timestamp}")
        print(
            "Tanggal-waktu  :",
            hasil_konversi.strftime("%d-%m-%Y %H:%M:%S"),
            "(waktu lokal)",
        )

    @staticmethod
    def tampilkan_waktu():
        waktu_sekarang = time.strftime("%H:%M:%S", time.localtime())
        print(f"Waktu lokal sekarang: {waktu_sekarang}")

    @staticmethod
    def jalankan_timer():
        teks_durasi = input("Durasi hitung mundur (1-10 detik): ").strip()

        try:
            durasi = int(teks_durasi)
        except ValueError:
            print("Durasi harus berupa bilangan bulat.")
            return

        if not 1 <= durasi <= 10:
            print("Durasi harus antara 1 dan 10 detik.")
            return

        for sisa_waktu in range(durasi, 0, -1):
            print(f"Sisa waktu: {sisa_waktu} detik")
            time.sleep(1)

        print("Waktu habis!")


if __name__ == "__main__":
    AplikasiPengelolaWaktu().jalankan()
