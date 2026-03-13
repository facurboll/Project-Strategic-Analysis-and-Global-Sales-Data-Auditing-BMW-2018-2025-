# 📊 Project: Strategic Analysis and Global Sales Data Auditing (BMW 2018-2025)

**Project Profile:** Data Analytics / Business Intelligence
**Tools & Technologies:** Python (Pandas, Seaborn, Matplotlib)

### 📌 1. Executive Summary
A comprehensive analysis of BMW's global commercial performance, evaluating revenue, sales volume, and the transition toward electric mobility (BEV). This project encompassed the entire data pipeline, from data ingestion via the Kaggle API to exploratory data analysis (EDA) and auditing, revealing key correlations between macroeconomic indicators and product strategies.

### 🧹 2. Data Quality & Auditing
A rigorous data cleaning and validation process was implemented to ensure analytical accuracy.
* **Integrity:** The dataset presented zero null values and no duplicated records.
* **Business Logic Audit:** Through the analysis of price variance (spread) and the mathematically perfect distribution of global revenue (exactly 25% per region), it was audited and proven that the data structure was artificially balanced and smoothed. This confirms the dataset is optimized for Time-Series Forecasting models, purposefully isolating historical anomalies (such as the 2020 global market crash).

### 💡 3. Key Insights
* **Economics Drives Ecology:** Utilizing a Correlation Heatmap and scatter plots, a near-perfect positive correlation (0.95) was demonstrated between the Fuel Price Index (`Fuel_Price_Index`) and electric vehicle adoption (`BEV_Share`). The data proves that consumers make the energy transition driven primarily by rising maintenance and running costs.
* **Revenue Composition:** The luxury BMW X7 leads the price ceiling (~€94,000), while the MINI brand (~€40,000) acts strategically as an entry-level product. However, global revenue is evenly sustained by mid and high-range models, showcasing a highly diversified and resilient product portfolio.

### 🎯 4. Conclusion & Strategic Recommendations
To maximize profitability in upcoming quarters, it is highly recommended to dynamically align the battery electric vehicle (BEV) supply chain with macroeconomic fuel price projections for each specific region. Aggressive marketing campaigns for models like the iX or i4 will yield the highest ROI (Return on Investment) in markets experiencing inflationary spikes in traditional energy costs.
