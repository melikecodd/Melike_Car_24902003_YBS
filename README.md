# Kişisel Finans ve Harcama Takip Sistemi

## Öğrenci Bilgileri

* Ad Soyad: Melike Çar
* Öğrenci No: 24902003
* Bölüm: Yönetim Bilişim Sistemleri (YBS)
* Ders: Python Programlama II
* Dönem: Bahar 2026

---

# Proje Amacı

Bu proje kullanıcıların gelir ve giderlerini kayıt altına almasını, finansal analizler yapmasını ve verileri grafiklerle görüntülemesini sağlayan modüler bir kişisel finans yönetim sistemidir.

Proje kapsamında:

* Gelir ekleme
* Gider ekleme
* İşlem listeleme
* İşlem silme
* CSV dosyasına kaydetme
* CSV dosyasından okuma
* Pandas ile analiz
* NumPy ile istatistiksel hesaplamalar
* Matplotlib ile grafik oluşturma
* GUI arayüzü

özellikleri geliştirilmiştir.

---

# Kullanılan Teknolojiler

* Python
* Pandas
* NumPy
* Matplotlib
* Tkinter
* CSV

---

# Proje Yapısı

Melike_Car_24902003_YBS/

├── main.py

├── finans_modeli.py

├── islem_yonetimi.py

├── dosya_islemleri.py

├── analiz.py

├── gorsellestirme.py

├── utils.py

├── veriler.csv

├── grafikler/

│ ├── bar_grafik.png

│ ├── pasta_grafik.png

│ └── aylik_grafik.png

└── README.md

---

# Kullanılan Veri Yapıları

Gelir ve gider kayıtları listeler içerisinde tutulmaktadır.

gelirler = []

giderler = []

Her kayıt bir Islem nesnesidir.

---

# Nesne Tabanlı Programlama

Projede Islem adlı bir sınıf oluşturulmuştur.

Bu sınıf:

* işlem ID
* işlem türü
* kategori
* tutar
* tarih

bilgilerini saklamaktadır.

---

# Pandas Analizleri

* Toplam gelir
* Toplam gider
* Net bakiye
* Aylık analiz
* Haftalık analiz

---

# NumPy Analizleri

* Ortalama harcama
* Minimum harcama
* Maksimum harcama
* Standart sapma

---

# Grafikler

1. Gelir-Gider Çubuk Grafiği
2. Gelir-Gider Pasta Grafiği
3. Aylık Gelir-Gider Çizgi Grafiği
## GUI Kullanımı

Proje Tkinter ile grafik arayüz desteklemektedir.
Kullanıcı gelir/gider ekleme, analiz ve grafik işlemlerini butonlar ile gerçekleştirebilir.

# Projenin çalıştığına dair ekran görüntüleri

---c:\Users\melik\Pictures\Screenshots\Ekran görüntüsü 2026-06-04 224709.png
![alt text](<Ekran görüntüsü 2026-06-04 224826.png>)


# GitHub Commitleri

Commit 1:
Proje klasör yapısı oluşturuldu

Commit 2:
Gelir ve gider yönetimi eklendi

Commit 3:
CSV ve analiz modülleri geliştirildi

Commit 4:
GUI ve grafik sistemleri tamamlandı

---
## Notlar

Bu proje Python Programlama II dersi kapsamında geliştirilmiştir.
Modüler yapı, OOP, CSV, Pandas, NumPy ve Matplotlib kullanılmıştır.