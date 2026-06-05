from datetime import datetime


def yeni_id_olustur(liste):
    """
    Yeni benzersiz ID oluşturur.
    """

    if not liste:
        return 1

    return max(islem.id for islem in liste) + 1


def tarih_kontrol(tarih):
    """
    Tarih formatı kontrolü
    YYYY-MM-DD
    """

    try:
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def sayi_kontrol(deger):
    """
    Sayısal değer kontrolü
    """

    try:
        float(deger)
        return True
    except ValueError:
        return False


def menu_goster():
    """
    Ana menü
    """

    print("\n")
    print("=" * 40)
    print("KİŞİSEL FİNANS TAKİP SİSTEMİ")
    print("=" * 40)

    print("1 - Gelir Ekle")
    print("2 - Gider Ekle")
    print("3 - İşlemleri Listele")
    print("4 - Analiz Yap")
    print("5 - Grafik Göster")
    print("6 - CSV Kaydet")
    print("7 - İşlem Sil")
    print("8 - Çıkış")

    print("=" * 40)