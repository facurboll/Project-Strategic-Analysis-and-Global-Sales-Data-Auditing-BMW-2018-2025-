# 📊 Strategic Analysis & Global Sales Data Auditing — BMW (2018–2025)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4c72b0)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> **Domain:** Business Intelligence | EDA | Macroeconomic Analysis | EV Strategy  
> **Tech Stack:** Python · Pandas · Seaborn · Matplotlib · Kaggle API

---

## 📌 Executive Summary

A comprehensive analysis of BMW's global commercial performance (2018–2025), evaluating revenue, sales volume, and the transition toward electric mobility (BEV). This project covers the full data pipeline — from ingestion via the **Kaggle API** to EDA and business auditing — revealing key correlations between macroeconomic indicators and product strategy outcomes.

**Key questions answered:**
- What drives EV adoption globally — policy or economics?
- How resilient is BMW's revenue across market shocks?
- Is the dataset suitable for forecasting, or does it hide structural anomalies?

---

## 📁 Project Structure

```
Project-Strategic-Analysis-and-Global-Sales-Data-Auditing-BMW-2018-2025-/
│
├── bmw_sales.ipynb    # Full EDA and auditing notebook
├── README.md
├── .gitignore
└── LICENSE
```

---

## 📊 Dataset

| Field | Detail |
|---|---|
| Source | [Kaggle – BMW Global Sales Dataset](https://www.kaggle.com/) |
| Period | 2018–2025 |
| Key columns | Region, Year, Model, Revenue (€), Units Sold, BEV Share, Fuel Price Index |

> ⚠️ *Update the source link above with the exact Kaggle URL used.*

---

## 🧹 Data Quality & Auditing

A rigorous validation process was implemented before any analysis:

| Check | Result |
|---|---|
| Null values | ✅ Zero nulls across all columns |
| Duplicate records | ✅ No duplicates found |
| Business logic audit | ⚠️ Revenue distribution was exactly 25% per region — artificially balanced |

**Key auditing finding:** The mathematically perfect regional revenue distribution (25% per region) reveals the dataset was intentionally smoothed and balanced — optimized for Time-Series Forecasting models, not raw transactional data. Historical anomalies like the 2020 global market crash were purposefully isolated. This was explicitly flagged as a data governance finding.

---

## 💡 Key Insights

### ⚡ Economics Drives Ecology — Correlation: Fuel Price Index vs BEV Adoption
Using a Correlation Heatmap and scatter plots, a near-perfect positive correlation (**r = 0.95**) was found between `Fuel_Price_Index` and `BEV_Share`. The data proves that consumer EV adoption is driven primarily by rising fuel and running costs — not by environmental incentives alone.

### 💰 Revenue Composition & Portfolio Resilience
| Segment | Price Range | Strategic Role |
|---|---|---|
| BMW X7 | ~€94,000 | Premium ceiling |
| Mid-range models (3, 5 Series) | ~€50–70K | Core revenue driver |
| MINI brand | ~€40,000 | Entry-level / volume |

Global revenue is evenly distributed across mid and high-range models, demonstrating a **highly diversified and resilient product portfolio** — not overly dependent on any single segment.

---

## 🎯 Strategic Recommendations

- **BEV supply chain alignment:** Dynamically align EV inventory with macroeconomic fuel price projections per region. High fuel price markets = highest BEV conversion potential.
- **Targeted marketing ROI:** iX and i4 models yield highest return in markets experiencing inflationary spikes in traditional energy costs.
- **Data governance note:** Future datasets should retain raw regional variance to enable realistic shock-scenario modeling (e.g., post-COVID demand recovery).

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/facurboll/Project-Strategic-Analysis-and-Global-Sales-Data-Auditing-BMW-2018-2025-.git
cd Project-Strategic-Analysis-and-Global-Sales-Data-Auditing-BMW-2018-2025-

# 2. Install dependencies
pip install pandas seaborn matplotlib jupyter kaggle

# 3. Download the dataset via Kaggle API
kaggle datasets download -d <dataset-slug>

# 4. Launch the notebook
jupyter notebook bmw_sales.ipynb
```

> 💡 You'll need a Kaggle account and API token (`~/.kaggle/kaggle.json`) to use the Kaggle CLI.

---

## 👤 Author

**Facundo Iván Ramírez Boll**  
Contador Público | Analista de Datos 🇦🇷  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/facundo-ramirez-boll-37849a227)
[![GitHub](https://img.shields.io/badge/GitHub-facurboll-black?logo=github)](https://github.com/facurboll)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
