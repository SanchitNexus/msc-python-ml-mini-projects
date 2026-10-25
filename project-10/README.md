## Macroeconomic Indicators Exploratory Data Analysis

### Problem Statement
Perform a reproducible exploratory audit of a multivariate US macroeconomic dataset.

### Dataset
`data/macrodata.csv`: **real historical US macroeconomic quarterly series**, sourced from the built-in `statsmodels.datasets.macrodata` dataset and bundled as CSV. Distinct from the other nine projects.

### Approach
Compute `.describe()` summaries, missing counts, IQR-based outlier counts and Pearson correlations; export CSV reports and a heatmap.

### Result
Verified offline run: **203 rows × 14 columns**, **0 missing values**, **22 IQR outliers** in the inflation column.

### Key Insight
Several macroeconomic series change together over decades; high correlation between trending economic variables does not establish a direct causal relationship, and trends should be considered before interpreting the heatmap.

### How to Run
`pip install -r requirements.txt` then `python main.py`. Works offline.
