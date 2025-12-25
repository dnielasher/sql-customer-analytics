-- 1. Gabungkan data User dan Order
-- 2. Hitung Metrik RFM per User
WITH rfm_base AS (
    SELECT 
        u.user_id,
        MAX(o.order_date) as last_order_date,
        COUNT(o.order_id) as frequency,
        SUM(o.amount) as monetary
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    GROUP BY u.user_id
),

-- 3. Tentukan Skor Recency (Hari sejak pembelian terakhir)
rfm_calc AS (
    SELECT 
        user_id,
        frequency,
        monetary,
        -- Anggap hari ini adalah 2024-06-01 untuk simulasi
        CAST(julianday('2024-06-01') - julianday(last_order_date) AS INTEGER) as recency_days
    FROM rfm_base
)

-- 4. Segmentasi User
SELECT 
    user_id,
    recency_days,
    frequency,
    monetary,
    CASE 
        WHEN frequency >= 10 AND monetary > 5000000 THEN 'VIP Customer'
        WHEN recency_days > 90 THEN 'Churn Risk' -- Tidak belanja 3 bulan
        WHEN recency_days <= 30 THEN 'Active User'
        ELSE 'Casual User'
    END as customer_segment
FROM rfm_calc
ORDER BY monetary DESC;