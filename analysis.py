
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_dir = Path(__file__).resolve().parent
output_dir = base_dir / "outputs"

# Membaca dataset
data_dir = base_dir / "data"
possible_files = [
    data_dir / "SampleSuperstore.csv",
    data_dir / "Sample - Superstore.csv",
]
file = next((path for path in possible_files if path.exists()), possible_files[0])

df = pd.read_csv(file, encoding="latin1")

# Membersihkan nama kolom dari spasi
df.columns = df.columns.str.strip()

print("Ukuran dataset:", df.shape)
print("\nNama kolom:")
print(df.columns.tolist())

# Memeriksa kualitas data
print("\nNilai kosong:")
print(df.isnull().sum())

print("\nData duplikat:", df.duplicated().sum())

# Menghapus data duplikat
df = df.drop_duplicates()

# Memastikan kolom numerik terbaca benar
for col in ["Sales", "Profit", "Quantity", "Discount"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["Sales", "Profit"])

# Analisis penjualan dan keuntungan
kategori = df.groupby("Category").agg(
    total_sales=("Sales", "sum"),
    total_profit=("Profit", "sum"),
    total_quantity=("Quantity", "sum")
).sort_values("total_sales", ascending=False)

wilayah = df.groupby("Region").agg(
    total_sales=("Sales", "sum"),
    total_profit=("Profit", "sum")
).sort_values("total_profit", ascending=False)

print("\nHasil berdasarkan kategori:")
print(kategori.round(2))

print("\nHasil berdasarkan wilayah:")
print(wilayah.round(2))

# Membuat folder hasil
output_dir.mkdir(exist_ok=True)

# Grafik penjualan dan keuntungan
kategori[["total_sales", "total_profit"]].plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Penjualan dan Keuntungan per Kategori")
plt.xlabel("Kategori")
plt.ylabel("Nilai")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output_dir / "analisis_kategori.png", dpi=150)
plt.close()

# Analisis produk dengan keuntungan terendah
produk = df.groupby("Sub-Category").agg(
    sales=("Sales", "sum"),
    profit=("Profit", "sum")
).sort_values("profit")

print("\nLima subkategori dengan keuntungan terendah:")
print(produk.head(5).round(2))

print("\nAnalisis selesai.")
