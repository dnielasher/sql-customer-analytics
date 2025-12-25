import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Setup Database (SQLite)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# 2. Buat Tabel
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    signup_date DATE,
    country TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_date DATE,
    amount REAL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
''')

# 3. Generate Data Dummy (100 User, 500 Transaksi)
print("Generating dummy data...")
users = []
start_date = datetime(2023, 1, 1)

for i in range(1, 101): # 100 User
    signup = start_date + timedelta(days=random.randint(0, 365))
    country = random.choice(['Indonesia', 'Singapore', 'Malaysia'])
    users.append((i, signup.strftime('%Y-%m-%d'), country))

cursor.executemany('INSERT OR IGNORE INTO users VALUES (?,?,?)', users)

orders = []
for i in range(1, 501): # 500 Order
    uid = random.randint(1, 100)
    # Order date harus setelah signup date
    user_signup = datetime.strptime(users[uid-1][1], '%Y-%m-%d')
    order_date = user_signup + timedelta(days=random.randint(0, 300))
    amount = round(random.uniform(50000, 2000000), 2) # Transaksi 50rb - 2jt
    orders.append((i, uid, order_date.strftime('%Y-%m-%d'), amount))

cursor.executemany('INSERT OR IGNORE INTO orders VALUES (?,?,?,?)', orders)

conn.commit()
print("Database 'ecommerce.db' berhasil dibuat dengan data dummy.")
conn.close()