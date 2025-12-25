# 🛒 E-Commerce Customer Segmentation (RFM Analysis)

Project ini melakukan analisis segmentasi pelanggan menggunakan teknik **RFM (Recency, Frequency, Monetary)** dengan **SQL**. Tujuannya adalah mengidentifikasi pelanggan VIP dan pelanggan yang berisiko churn.

## 📂 Struktur Project
* `generate_data.py`: Script Python untuk membuat Dummy Data (Users & Orders) ke dalam database SQLite.
* `analysis_query.sql`: Kumpulan Query SQL kompleks (CTE, Aggregation, CASE WHEN) untuk analisis.
* `run_analysis.py`: Script untuk mengeksekusi query dan menyimpan hasil ke CSV.

## 📊 Metodologi (RFM)
Analisis dilakukan berdasarkan 3 pilar:
1.  **Recency:** Berapa hari sejak pembelian terakhir?
2.  **Frequency:** Berapa kali user bertransaksi?
3.  **Monetary:** Berapa total uang yang dibelanjakan?

## 💡 Key SQL Concepts Used
* **CTEs (Common Table Expressions)** untuk struktur query yang rapi.
* **Joins** untuk menghubungkan tabel Users dan Orders.
* **Window Functions & Date Manipulation** untuk menghitung selisih hari.
* **Conditional Logic (CASE WHEN)** untuk pelabelan segmen (VIP vs Churn).

## 🚀 Cara Menjalankan
1.  Jalankan `python generate_data.py` untuk membuat database.
2.  Jalankan `python run_analysis.py` untuk melihat hasil analisis.