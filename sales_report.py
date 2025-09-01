
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np, random

BASE = "sales-report-portfolio"
OUT = os.path.join(BASE, "outputs")
CSV = os.path.join(BASE, "sales_data.csv")
os.makedirs(OUT, exist_ok=True)

# CSVが無ければ作る
if not os.path.exists(CSV):
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=100, freq="D")
    stores = ["Tokyo", "Osaka", "Nagoya"]
    products = ["Apple","Banana","Orange","Grapes","Peach"]
    data = []
    for d in dates:
        for _ in range(random.randint(1, 3)):
            store = random.choice(stores)
            product = random.choice(products)
            quantity = random.randint(1, 20)
            price = random.randint(80, 300)
            amount = quantity * price
            data.append([d.strftime("%Y-%m-%d"), store, product, amount, quantity])
    df = pd.DataFrame(data, columns=["date","store","product","amount","quantity"])
    df = df.sample(100, random_state=42).reset_index(drop=True)
    df.to_csv(CSV, index=False, encoding="utf-8-sig")
    print("generated CSV:", CSV)

# 読み込み
df = pd.read_csv(CSV, encoding="utf-8-sig")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# 集計
monthly_sales = df.groupby("month")["amount"].sum()
top5_products = df.groupby("product")["amount"].sum().sort_values(ascending=False).head(5)
store_sales   = df.groupby("store")["amount"].sum()
weekday_sales = df.groupby(df["date"].dt.day_name())["amount"].sum()

# グラフ（色指定なし）
plt.figure(figsize=(8,4))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales"); plt.xlabel("Month"); plt.ylabel("Sales Amount"); plt.grid(True); plt.tight_layout()
plt.savefig(os.path.join(OUT, "monthly_sales.png")); plt.close()

plt.figure(figsize=(8,4))
top5_products.plot(kind="barh")
plt.title("Top 5 Products by Sales"); plt.xlabel("Sales Amount"); plt.ylabel("Product"); plt.tight_layout()
plt.savefig(os.path.join(OUT, "top5_products.png")); plt.close()

plt.figure(figsize=(6,6))
store_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.ylabel(""); plt.title("Sales Share by Store"); plt.tight_layout()
plt.savefig(os.path.join(OUT, "store_share.png")); plt.close()

weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
plt.figure(figsize=(8,4))
weekday_sales.reindex(weekday_order).plot(kind="bar", rot=0)
plt.title("Sales by Weekday"); plt.xlabel("Weekday"); plt.ylabel("Sales Amount"); plt.tight_layout()
plt.savefig(os.path.join(OUT, "weekday_sales.png")); plt.close()

# Excel出力
excel_path = os.path.join(OUT, "aggregated_tables.xlsx")
with pd.ExcelWriter(excel_path, engine="xlsxwriter") as w:
    monthly_sales.to_frame("amount").to_excel(w, sheet_name="monthly_sales")
    df.groupby("product")["amount"].sum().sort_values(ascending=False).to_frame("amount").to_excel(w, sheet_name="product_sales_all")
    top5_products.to_frame("amount").to_excel(w, sheet_name="product_top5")
    store_sales.to_frame("amount").to_excel(w, sheet_name="store_sales")
    weekday_sales.to_frame("amount").to_excel(w, sheet_name="weekday_sales")

print("✅ Done. See:", OUT)
