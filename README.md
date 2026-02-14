# 📊 Sales Data Analysis Dashboard

A beginner-friendly Python project that generates a sample sales dataset,
cleans it with **Pandas**, and visualises key metrics with **Matplotlib**.

---

## 🗂 Project Structure

```
sales-dashboard/
├── sales_analysis.py   ← Main script (generate → load → clean → analyse → plot)
├── sales.csv           ← Auto-generated sample dataset (500 rows)
├── requirements.txt    ← Python dependencies
└── README.md           ← You are here
```

---

## 🚀 Quick Start

### 1. Clone / download the project files

### 2. (Recommended) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python sales_analysis.py
```

The script will:
- Regenerate `sales.csv` with fresh sample data
- Print summary stats to the terminal
- Save `sales_dashboard.png` with two charts
- Display an interactive chart window

---

## 📈 What the Script Does

| Step | What happens |
|------|-------------|
| **Generate** | Creates 500 fake sales records for 10 products across 2024 and saves them to `sales.csv` |
| **Load** | Reads `sales.csv` with `pd.read_csv()` and parses date columns |
| **Clean** | Detects ~5 % intentionally missing `quantity` values and fills them with per-product median |
| **Analyse** | Calculates total revenue, monthly revenue, and the top-5 products by revenue |
| **Visualise** | Plots a monthly bar chart and a top-products horizontal bar chart |

---

## 📊 Output Charts

### Monthly Revenue Bar Chart
Shows how revenue varied month-by-month throughout 2024.

### Top 5 Products by Revenue
Horizontal bar chart ranking the best-selling products.

---

## 🧩 Key Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, cleaning, grouping |
| `numpy` | Random data generation |
| `matplotlib` | Bar charts and figure layout |

---

## 💡 Ideas to Extend This Project

- Add a **pie chart** showing revenue share by product category
- Filter data by **date range** using command-line arguments
- Export the summary stats to a formatted **Excel report**
- Build an interactive dashboard with **Plotly** or **Streamlit**

---

## 📋 Requirements

- Python 3.8+
- See `requirements.txt` for library versions
