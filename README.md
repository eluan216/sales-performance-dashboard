# Sales Performance Analytics Dashboard

End-to-end retail sales analytics: generate data, clean it, and answer core business questions with Python.

**Author:** Oguma Eluanatein Odo

---

## Quick Start (anyone can run this)

```bash
git clone https://github.com/eluan216/sales-performance-dashboard.git
cd sales-performance-dashboard
pip install -r requirements.txt
python src/generate_and_analyze.py
```

This will:

1. Generate synthetic retail sales data
2. Clean and validate it
3. Save CSVs under `Data/`
4. Print revenue/profit by region, category, top products, top customers, and monthly trend

No external dataset required.

---

## Project Overview

Businesses generate large volumes of transactional data. This project demonstrates the analytics lifecycle:

1. Data generation / ingestion
2. Cleaning & validation
3. Business analysis (region, category, customers, trends)
4. Export of analysis-ready CSVs for Excel / Power BI

---

## Business Questions Answered

- Which region generates the highest sales?
- Which categories and products drive revenue and profit?
- Who are the top customers?
- How do sales trend month by month?

---

## Tech Stack

| Layer         | Tools                |
|---------------|----------------------|
| Pipeline      | Python, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Power BI (optional) |
| Spreadsheet   | Excel (load the CSVs) |

---

## Repository Structure

```text
sales-performance-dashboard/
├── Data/                      # Generated raw + clean CSVs
├── src/
│   └── generate_and_analyze.py
├── Sql/                       # Optional SQL examples
├── Notebooks/                 # Optional notebooks
├── Dashboard/                 # Power BI files (add your own)
├── Images/                    # Screenshots
├── requirements.txt
└── README.md
```

---

## Optional next steps

After running the script:

1. Open `Data/sales_clean.csv` in Excel or Power BI
2. Build KPIs: Total Revenue, Total Profit, Sales by Region, Trend, Top Products
3. Add dashboard screenshots under `Images/`

---

## Author

**Oguma Eluanatein Odo**  
B.Sc. Biomedical Technology · Data Analytics & AI  
[LinkedIn](https://linkedin.com/in/eluanatein-oguma-5552571b6) · [GitHub](https://github.com/eluan216) · ogumaeluan@gmail.com

---

## License

MIT
