import sqlite3
import pandas as pd

# Koneksi ke DB
conn = sqlite3.connect('ecommerce.db')

# Baca Query dari file .sql
with open('analysis_query.sql', 'r') as file:
    query = file.read()

# Eksekusi Query menggunakan Pandas
df_result = pd.read_sql_query(query, conn)

# Tampilkan Hasil
print("Hasil Analisis RFM:")
print(df_result.head(10))
print("\nJumlah User per Segmen:")
print(df_result['customer_segment'].value_counts())

# Simpan ke CSV untuk Portofolio
df_result.to_csv('rfm_analysis_result.csv', index=False)
print("\nHasil tersimpan ke 'rfm_analysis_result.csv'")

conn.close()