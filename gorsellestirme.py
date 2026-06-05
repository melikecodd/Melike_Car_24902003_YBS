import matplotlib.pyplot as plt


def gelir_gider_bar(df):

    gelir = (
        df[df["Tur"] == "Gelir"]["Tutar"]
        .sum()
    )

    gider = (
        df[df["Tur"] == "Gider"]["Tutar"]
        .sum()
    )

    plt.figure(figsize=(6, 4))

    plt.bar(
        ["Gelir", "Gider"],
        [gelir, gider]
    )

    plt.title("Gelir - Gider Karşılaştırması")
    plt.ylabel("TL")

    plt.savefig("bar_grafik.png")

    plt.show()


def pasta_grafik(df):

    gelir = (
        df[df["Tur"] == "Gelir"]["Tutar"]
        .sum()
    )

    gider = (
        df[df["Tur"] == "Gider"]["Tutar"]
        .sum()
    )

    plt.figure(figsize=(6, 6))

    plt.pie(
        [gelir, gider],
        labels=["Gelir", "Gider"],
        autopct="%1.1f%%"
    )

    plt.title("Gelir - Gider Oranları")

    plt.savefig("pasta_grafik.png")

    plt.show()


def aylik_grafik(df):

    df["Ay"] = df["Tarih"].dt.to_period("M")

    aylik = (
        df.groupby(["Ay", "Tur"])["Tutar"]
        .sum()
        .unstack(fill_value=0)
    )

    aylik.plot(
        kind="line",
        figsize=(8, 5),
        marker="o"
    )

    plt.title("Aylık Gelir ve Gider Analizi")
    plt.ylabel("TL")

    plt.savefig("aylik_grafik.png")

    plt.show()