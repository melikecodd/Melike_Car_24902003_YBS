import pandas as pd
import numpy as np


def verileri_dataframe_yap(gelirler, giderler):

    veriler = []

    for gelir in gelirler:
        veriler.append(gelir.to_dict())

    for gider in giderler:
        veriler.append(gider.to_dict())

    df = pd.DataFrame(veriler)

    if not df.empty:
        df["Tarih"] = pd.to_datetime(df["Tarih"])

    return df


def toplam_gelir_gider(df):

    toplam_gelir = df[df["Tur"] == "Gelir"]["Tutar"].sum()

    toplam_gider = df[df["Tur"] == "Gider"]["Tutar"].sum()

    net_bakiye = toplam_gelir - toplam_gider

    print("\n===== FİNANSAL ÖZET =====")
    print(f"Toplam Gelir : {toplam_gelir:.2f} TL")
    print(f"Toplam Gider : {toplam_gider:.2f} TL")
    print(f"Net Bakiye   : {net_bakiye:.2f} TL")

    return toplam_gelir, toplam_gider


def aylik_analiz(df):

    if df.empty:
        print("Veri bulunamadı.")
        return

    df["Ay"] = df["Tarih"].dt.to_period("M")

    sonuc = (
        df.groupby(["Ay", "Tur"])["Tutar"]
        .sum()
        .unstack(fill_value=0)
    )

    print("\n===== AYLIK ANALİZ =====")
    print(sonuc)

    return sonuc


def numpy_istatistik(df):

    giderler = df[df["Tur"] == "Gider"]["Tutar"]

    if len(giderler) == 0:
        print("Gider verisi bulunamadı.")
        return

    print("\n===== NUMPY İSTATİSTİKLERİ =====")

    print("Ortalama:",
          np.mean(giderler))

    print("Minimum:",
          np.min(giderler))

    print("Maksimum:",
          np.max(giderler))

    print("Standart Sapma:",
          np.std(giderler))
