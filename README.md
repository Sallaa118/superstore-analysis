# Superstore Sales Data Analysis

## 📌 Deskripsi Proyek

Proyek ini merupakan analisis data penjualan menggunakan Python dan dataset Superstore. Tujuan proyek adalah memahami pola penjualan, keuntungan, kategori produk, dan performa wilayah melalui proses eksplorasi dan analisis data.

Proyek ini dibuat sebagai latihan **Data Analytics** untuk mempelajari proses pengolahan data, pemeriksaan kualitas data, agregasi, serta interpretasi hasil analisis untuk mendukung pengambilan keputusan bisnis.

## 🎯 Tujuan Analisis

1. Memahami struktur dan karakteristik dataset penjualan.
2. Memeriksa nilai kosong dan data duplikat.
3. Mengidentifikasi kategori produk dengan penjualan dan keuntungan tertinggi.
4. Membandingkan performa penjualan dan keuntungan antarwilayah.
5. Menemukan subkategori produk dengan keuntungan terendah.
6. Menghasilkan insight yang dapat digunakan sebagai dasar analisis bisnis lebih lanjut.

## 📂 Struktur Proyek

```text
superstore-analysis/
├── data/
│   └── Sample - Superstore.csv
├── analysis.py
├── README.md
├── requirements.txt
└── .gitignore
```

Catatan: Folder `.venv/` digunakan untuk environment Python lokal dan tidak perlu diunggah ke GitHub. Sesuaikan nama dan lokasi file dataset dengan struktur folder yang digunakan.

## 📊 Dataset

Dataset yang digunakan adalah Superstore Sales Dataset, yang berisi informasi transaksi penjualan, pelanggan, produk, wilayah, diskon, dan keuntungan.

Sumber dataset: [Sample Superstore Dataset – Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

Dataset memiliki 21 kolom, di antaranya:

- `Order Date`: tanggal pemesanan.
- `Customer Name`: nama pelanggan.
- `Region`: wilayah penjualan.
- `Category`: kategori produk.
- `Sub-Category`: subkategori produk.
- `Sales`: nilai penjualan.
- `Quantity`: jumlah barang terjual.
- `Discount`: diskon.
- `Profit`: keuntungan atau kerugian.

## 🛠️ Teknologi yang Digunakan

- **Python** — bahasa pemrograman untuk analisis data.
- **Pandas** — membaca, mengolah, membersihkan, dan mengagregasi data.
- **Matplotlib** — membuat visualisasi data.
- **Seaborn** — membantu membuat visualisasi statistik.

## ⚙️ Cara Menjalankan Proyek

### 1. Clone repository

```bash
git clone <URL_REPOSITORY>
cd superstore-analysis
```

Ganti `<URL_REPOSITORY>` dengan URL repository GitHub milikmu.

### 2. Buat virtual environment

```bash
python -m venv .venv
```

Aktifkan environment pada Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instal library

```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum tersedia, instal library secara langsung:

```bash
pip install pandas matplotlib seaborn
```

### 4. Siapkan dataset

Unduh dataset dari sumber yang dicantumkan di atas. Letakkan file CSV di folder `data/`, lalu pastikan variabel lokasi file pada `analysis.py` sesuai dengan lokasi dataset.

Contoh:

```python
file = "data/Sample - Superstore.csv"
```

### 5. Jalankan analisis

```bash
python analysis.py
```

Program akan menampilkan informasi struktur kolom, pemeriksaan data kosong dan duplikat, agregasi penjualan dan keuntungan berdasarkan kategori serta wilayah, dan daftar subkategori dengan keuntungan terendah.

## 🔎 Hasil Analisis

### 1. Kualitas Data

- Jumlah kolom: 21.
- Nilai kosong yang terdeteksi: 0.
- Baris duplikat yang terdeteksi: 0.

Berdasarkan pemeriksaan awal, tidak ditemukan nilai kosong maupun baris duplikat pada dataset.

### 2. Analisis Kategori Produk

| Kategori | Total Sales | Total Profit |
|---|---:|---:|
| Technology | 836,154.03 | 145,454.95 |
| Furniture | 741,999.80 | 18,451.27 |
| Office Supplies | 719,047.03 | 122,490.80 |

**Insight:**

- Technology memiliki total penjualan dan keuntungan tertinggi.
- Furniture memiliki nilai penjualan cukup besar, tetapi keuntungan relatif rendah.
- Office Supplies mencatat jumlah barang terjual tertinggi, yaitu 22,906 unit.

### 3. Analisis Wilayah

| Region | Total Sales | Total Profit |
|---|---:|---:|
| West | 725,457.82 | 108,418.45 |
| East | 678,781.24 | 91,522.78 |
| South | 391,721.90 | 46,749.43 |
| Central | 501,239.89 | 39,706.36 |

**Insight:**

- West merupakan wilayah dengan total penjualan dan keuntungan tertinggi.
- South memiliki total penjualan terendah.
- Central memiliki penjualan lebih tinggi daripada South, tetapi keuntungan lebih rendah.

Perbedaan ini dapat menjadi dasar untuk menyelidiki pengaruh diskon, jenis produk, dan karakteristik transaksi pada setiap wilayah.

### 4. Analisis Subkategori dengan Keuntungan Terendah

| Sub-Category | Sales | Profit |
|---|---:|---:|
| Tables | 206,965.53 | -17,725.48 |
| Bookcases | 114,880.00 | -3,472.56 |
| Supplies | 46,673.54 | -1,189.10 |
| Fasteners | 3,024.28 | 949.52 |
| Machines | 189,238.63 | 3,384.76 |

**Insight:**

- Tables memiliki total kerugian terbesar.
- Bookcases dan Supplies juga memiliki keuntungan negatif.
- Fasteners dan Machines masih menghasilkan keuntungan positif, tetapi termasuk lima subkategori dengan nilai keuntungan terendah.

Temuan ini menunjukkan bahwa penjualan yang tinggi tidak selalu menghasilkan keuntungan yang tinggi.

## 💡 Kesimpulan

Analisis awal menunjukkan bahwa performa penjualan dan keuntungan berbeda berdasarkan kategori produk dan wilayah.

Technology merupakan kategori dengan keuntungan tertinggi, sedangkan Tables memiliki kerugian terbesar di antara subkategori yang dianalisis. Selain itu, perbedaan performa antarwilayah menunjukkan bahwa nilai penjualan saja belum cukup untuk menilai kinerja bisnis.

Hasil ini dapat dikembangkan lebih lanjut melalui analisis diskon, tren penjualan berdasarkan waktu, performa produk, dan hubungan antara penjualan dengan keuntungan.

## 🚀 Pengembangan Selanjutnya

- Membuat grafik penjualan dan keuntungan yang lebih lengkap.
- Menganalisis tren penjualan bulanan dan tahunan.
- Memeriksa hubungan antara diskon dan keuntungan.
- Mengidentifikasi produk yang paling menguntungkan dan merugikan.
- Membuat dashboard interaktif menggunakan Streamlit atau Power BI.

## ⚠️ Catatan

Hasil analisis merupakan temuan deskriptif dari dataset yang digunakan. Temuan tersebut belum membuktikan hubungan sebab-akibat. Interpretasi juga bergantung pada kualitas, cakupan, dan satuan mata uang dataset asli.

---

**Project Category:** Data Analytics  
**Language:** Python  
**Status:** Initial exploratory data analysis completed
