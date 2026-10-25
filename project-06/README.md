## Monthly Temperature Trend Forecast (Open-Meteo API)

### Problem Statement
Explore monthly temperature changes and predict the next month's average using a simple baseline.

### Dataset
**Free API #2:** [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), no API key; requests Delhi daily mean temperature 2022–2024 and groups to months. Offline fallback `data/elnino_monthly.csv` is a different **real historical Pacific sea-surface temperature series** from `statsmodels.datasets.elnino`, not Delhi measurements. The printed source identifies which dataset was used.

### Approach
Convert daily values to monthly means, use rolling 3-month average, and forecast one month ahead from last three recorded months. Save trend line PNG; simple baseline, not seasonally adjusted.

### Result
Verified offline run: **20.75 °C** next-month baseline forecast for the bundled Pacific series (not Delhi).

### Key Insight
A three-month moving average reduces short-term noise but lags abrupt temperature shifts, and it misses recurring seasonal cycles; this makes it an interpretable baseline rather than an accurate climate forecast.

### How to Run
`pip install -r requirements.txt` then `python main.py` or `python main.py --offline`.
