class Islem:
    """
    Gelir ve gider işlemlerini temsil eden sınıf
    """

    def __init__(self, id, tur, kategori, tutar, tarih):
        self.id = id
        self.tur = tur
        self.kategori = kategori
        self.tutar = float(tutar)
        self.tarih = tarih

    def to_dict(self):
        return {
            "ID": self.id,
            "Tur": self.tur,
            "Kategori": self.kategori,
            "Tutar": self.tutar,
            "Tarih": self.tarih
        }

    def __str__(self):
        return (
            f"ID:{self.id} | "
            f"{self.tur} | "
            f"{self.kategori} | "
            f"{self.tutar} TL | "
            f"{self.tarih}"
        )