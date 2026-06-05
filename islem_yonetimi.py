from finans_modeli import Islem
from utils import yeni_id_olustur, tarih_kontrol, sayi_kontrol


def gelir_ekle(gelirler):
    try:
        kategori = input("Gelir kategorisi: ")
        tutar = input("Tutar: ")
        tarih = input("Tarih (YYYY-MM-DD): ")

        if not sayi_kontrol(tutar):
            print("Hatalı tutar!")
            return

        if not tarih_kontrol(tarih):
            print("Hatalı tarih!")
            return

        yeni_gelir = Islem(
            yeni_id_olustur(gelirler),
            "Gelir",
            kategori,
            float(tutar),
            tarih
        )

        gelirler.append(yeni_gelir)

        print("Gelir başarıyla eklendi.")

    except Exception as hata:
        print("Hata:", hata)


def gider_ekle(giderler):
    try:
        kategori = input("Gider kategorisi: ")
        tutar = input("Tutar: ")
        tarih = input("Tarih (YYYY-MM-DD): ")

        if not sayi_kontrol(tutar):
            print("Hatalı tutar!")
            return

        if not tarih_kontrol(tarih):
            print("Hatalı tarih!")
            return

        yeni_gider = Islem(
            yeni_id_olustur(giderler),
            "Gider",
            kategori,
            float(tutar),
            tarih
        )

        giderler.append(yeni_gider)

        print("Gider başarıyla eklendi.")

    except Exception as hata:
        print("Hata:", hata)


def islemleri_listele(gelirler, giderler):

    print("\n===== GELİRLER =====")

    for gelir in gelirler:
        print(gelir)

    print("\n===== GİDERLER =====")

    for gider in giderler:
        print(gider)


def islem_sil(gelirler, giderler, silinecek_id):

    for gelir in gelirler:

        if gelir.id == silinecek_id:
            gelirler.remove(gelir)
            print("Gelir silindi.")
            return

    for gider in giderler:

        if gider.id == silinecek_id:
            giderler.remove(gider)
            print("Gider silindi.")
            return

    print("İşlem bulunamadı.")