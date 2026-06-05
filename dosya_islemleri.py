import csv
from finans_modeli import Islem


def csv_kaydet(dosya_adi, gelirler, giderler):

    with open(dosya_adi, "w", newline="", encoding="utf-8") as dosya:

        yazici = csv.writer(dosya)

        yazici.writerow(
            ["ID", "Tur", "Kategori", "Tutar", "Tarih"]
        )

        for gelir in gelirler:

            yazici.writerow([
                gelir.id,
                gelir.tur,
                gelir.kategori,
                gelir.tutar,
                gelir.tarih
            ])

        for gider in giderler:

            yazici.writerow([
                gider.id,
                gider.tur,
                gider.kategori,
                gider.tutar,
                gider.tarih
            ])

    print("CSV dosyasına kaydedildi.")


def csv_oku(dosya_adi):

    gelirler = []
    giderler = []

    try:

        with open(
            dosya_adi,
            "r",
            encoding="utf-8"
        ) as dosya:

            okuyucu = csv.DictReader(dosya)

            for satir in okuyucu:

                islem = Islem(
                    int(satir["ID"]),
                    satir["Tur"],
                    satir["Kategori"],
                    float(satir["Tutar"]),
                    satir["Tarih"]
                )

                if satir["Tur"] == "Gelir":
                    gelirler.append(islem)
                else:
                    giderler.append(islem)

    except FileNotFoundError:
        print("CSV dosyası bulunamadı.")

    return gelirler, giderler