-- Sample business questions for sales_clean.csv
-- Load the CSV into SQLite or any SQL engine first.

-- 1. Revenue and profit by region
SELECT region,
       ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;

-- 2. Profit by category
SELECT category,
       ROUND(SUM(profit), 2) AS total_profit,
       ROUND(AVG(profit), 2) AS avg_profit
FROM sales
GROUP BY category
ORDER BY total_profit DESC;

-- 3. Top 10 products by revenue
SELECT product,
       ROUND(SUM(revenue), 2) AS total_revenue,
       SUM(quantity) AS units_sold
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 10;

-- 4. Top customers
SELECT customer_id,
       ROUND(SUM(revenue), 2) AS total_revenue,
       COUNT(*) AS orders
FROM sales
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;

-- 5. Monthly revenue trend
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month;
