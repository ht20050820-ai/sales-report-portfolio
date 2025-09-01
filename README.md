# sales-report-portfolio


# 売上データ集計レポート（ポートフォリオ）

このリポジトリは、売上データを用いた **集計・可視化レポート** のサンプルです。  
クラウドソーシング応募時に「成果物イメージ」を共有するために作成しました。

## 内容
- **データ:** `sales_data.csv`（サンプル100行）
- **処理:**
  - 月別売上推移（折れ線）
  - 商品別売上トップ5（横棒）
  - 店舗別売上シェア（円）
  - 曜日別売上（棒）

## 成果物
- レポート（DOCX）: [Sales_Report_Portfolio.pdf](./Sales_Report_Portfolio.pdf)
- Jupyter Notebook: [sales_report_notebook.ipynb](./sales_report_notebook.ipynb)
- Pythonスクリプト: [sales_report.py](./sales_report.py)

## サンプル出力
![月別売上](./outputs/monthly_sales.png)

## 使い方（ローカル実行）
```bash
# 依存ライブラリ
pip install pandas matplotlib xlsxwriter

# スクリプト実行（outputs/ に画像とExcelが出力されます）
python sales_report.py


.
├─ sales_report.py
├─ sales_report_notebook.ipynb
├─ Sales_Report_Portfolio.pdf   
├─ sales_data.csv
├─ outputs/
│   ├─ monthly_sales.png
│   ├─ top5_products.png
│   ├─ store_share.png
│   ├─ weekday_sales.png
│   └─ aggregated_tables.xlsx
└─ README.md

