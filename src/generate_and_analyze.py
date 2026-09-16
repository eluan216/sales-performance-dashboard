"""
Sales Performance Analytics — runnable demo

Generates synthetic retail sales data, cleans it, runs EDA-style summaries,
and answers core business questions with Pandas (SQL-style aggregations).

Usage:
    pip install -r requirements.txt
    python src/generate_and_analyze.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data"
DATA_DIR.mkdir(exist_ok=True)


def generate_sales_data(n: int = 1500, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    regions = ["North", "South", "East", "West"]
    categories = ["Electronics", "Furniture", "Office Supplies", "Clothing"]
    products = {
        "Electronics": ["Laptop", "Monitor", "Headphones", "Keyboard"],
        "Furniture": ["Chair", "Desk", "Shelf", "Cabinet"],
        "Office Supplies": ["Paper", "Pens", "Notebook", "Stapler"],
        "Clothing": ["Shirt", "Jacket", "Shoes", "Hat"],
    }

    rows = []
    start = pd.Timestamp("2024-01-01")
    for i in range(n):
        cat = rng.choice(categories)
        product = rng.choice(products[cat])
        region = rng.choice(regions)
        quantity = int(rng.integers(1, 8))
        unit_price = float(rng.uniform(10, 400))
        discount = float(rng.choice([0, 0.05, 0.1, 0.15], p=[0.6, 0.2, 0.15, 0.05]))
        revenue = quantity * unit_price * (1 - discount)
        cost = revenue * float(rng.uniform(0.45, 0.75))
        profit = revenue - cost
        date = start + pd.Timedelta(days=int(rng.integers(0, 365)))
        customer = f"CUST-{int(rng.integers(1000, 1100))}"
        rows.append(
            {
                "order_id": f"ORD-{10000 + i}",
                "order_date": date.date().isoformat(),
                "region": region,
                "category": cat,
                "product": product,
                "customer_id": customer,
                "quantity": quantity,
                "unit_price": round(unit_price, 2),
                "discount": discount,
                "revenue": round(revenue, 2),
                "profit": round(profit, 2),
            }
        )
    return pd.DataFrame(rows)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["order_date"] = pd.to_datetime(out["order_date"])
    out = out.drop_duplicates(subset=["order_id"])
    out = out[out["quantity"] > 0]
    out = out[out["revenue"] >= 0]
    return out.reset_index(drop=True)


def business_insights(df: pd.DataFrame) -> None:
    print("=" * 56)
    print("SALES PERFORMANCE ANALYTICS — SUMMARY")
    print("=" * 56)
    print(f"Orders:          {len(df):,}")
    print(f"Total Revenue:   ${df['revenue'].sum():,.2f}")
    print(f"Total Profit:    ${df['profit'].sum():,.2f}")
    print(f"Avg Order Value: ${df['revenue'].mean():,.2f}")
    print()

    print("Revenue by Region")
    print(df.groupby("region")["revenue"].sum().sort_values(ascending=False).round(2).to_string())
    print()

    print("Profit by Category")
    print(df.groupby("category")["profit"].sum().sort_values(ascending=False).round(2).to_string())
    print()

    print("Top 5 Products by Revenue")
    print(
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .round(2)
        .to_string()
    )
    print()

    print("Top 5 Customers by Revenue")
    print(
        df.groupby("customer_id")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .round(2)
        .to_string()
    )
    print()

    monthly = (
        df.set_index("order_date")
        .resample("ME")["revenue"]
        .sum()
        .round(2)
    )
    print("Monthly Revenue Trend")
    print(monthly.to_string())
    print("=" * 56)


def main() -> None:
    raw = generate_sales_data()
    clean_df = clean(raw)

    raw_path = DATA_DIR / "sales_raw.csv"
    clean_path = DATA_DIR / "sales_clean.csv"
    raw.to_csv(raw_path, index=False)
    clean_df.to_csv(clean_path, index=False)

    print(f"Saved raw data  → {raw_path}")
    print(f"Saved clean data → {clean_path}")
    business_insights(clean_df)
    print("\nNext steps for a full portfolio version:")
    print("  - Load sales_clean.csv into Power BI / Excel")
    print("  - Add SQL scripts under Sql/")
    print("  - Export dashboard screenshots to Images/")


if __name__ == "__main__":
    main()
