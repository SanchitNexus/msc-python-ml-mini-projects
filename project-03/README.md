## Socioeconomic Country Clustering (World Bank API)

### Problem Statement
Group countries with similar development profiles without using known categories.

### Dataset
**Free API #1:** [World Bank Indicators API](https://api.worldbank.org/v2/), no key. Latest available GDP per capita (USD), life expectancy (years), and population for 12 named countries. Fallback `data/gapminder_2007.csv` is **real historical** Gapminder data bundled from Plotly's Gapminder sample; its values are from 2007, not current. No literacy field is claimed.

### Approach
Log-transform skewed GDP and population, standardize three indicators, and assign three KMeans clusters. Country samples are intentionally small for class demonstration.

### Result
Verified offline run: **12 countries** split into three clusters using the 2007 bundled snapshot.

### Key Insight
Raw population differs by orders of magnitude; using it unscaled would cause population size, not socioeconomic similarity, to dominate cluster membership.

### How to Run
`pip install -r requirements.txt` then `python main.py` (live API, automatic fallback) or `python main.py --offline` (bundled data).
