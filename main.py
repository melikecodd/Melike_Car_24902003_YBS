import tkinter as tk
from tkinter import messagebox

from islem_yonetimi import gelir_ekle, gider_ekle
from dosya_islemleri import csv_kaydet, csv_oku
from analiz import (
    verileri_dataframe_yap,
    toplam_gelir_gider,
    aylik_analiz,
    numpy_istatistik
)
from gorsellestirme import (
    gelir_gider_bar,
    pasta_grafik,
    aylik_grafik
)

# CSV'den verileri yükle (otomatik başlatma)
gelirler, giderler = csv_oku("veriler.csv")


def gui():

    def gelir_btn():
        gelir_ekle(gelirler)
        messagebox.showinfo("Başarılı", "Gelir eklendi")

    def gider_btn():
        gider_ekle(giderler)
        messagebox.showinfo("Başarılı", "Gider eklendi")

    def liste_btn():
        messagebox.showinfo("Bilgi", "Listeyi konsoldan kontrol edebilirsiniz")

    def analiz_btn():
        df = verileri_dataframe_yap(gelirler, giderler)
        toplam_gelir_gider(df)
        aylik_analiz(df)
        numpy_istatistik(df)
        messagebox.showinfo("Analiz", "Analiz tamamlandı")

    def grafik_btn():
        df = verileri_dataframe_yap(gelirler, giderler)
        gelir_gider_bar(df)
        pasta_grafik(df)
        aylik_grafik(df)
        messagebox.showinfo("Grafik", "Grafikler oluşturuldu")

    def kaydet_btn():
        csv_kaydet("veriler.csv", gelirler, giderler)
        messagebox.showinfo("CSV", "Veriler kaydedildi")

    root = tk.Tk()
    root.title("Kişisel Finans Takip Sistemi")
    root.geometry("450x450")

    tk.Label(
        root,
        text="KİŞİSEL FİNANS SİSTEMİ",
        font=("Arial", 16)
    ).pack(pady=15)

    tk.Button(root, text="Gelir Ekle", width=25, command=gelir_btn).pack(pady=5)
    tk.Button(root, text="Gider Ekle", width=25, command=gider_btn).pack(pady=5)
    tk.Button(root, text="Analiz Yap", width=25, command=analiz_btn).pack(pady=5)
    tk.Button(root, text="Grafik Göster", width=25, command=grafik_btn).pack(pady=5)
    tk.Button(root, text="CSV Kaydet", width=25, command=kaydet_btn).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    gui()
