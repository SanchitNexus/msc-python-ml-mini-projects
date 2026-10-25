## Car-Sharing Usage Visual Dashboard

### Problem Statement
Explore when and where car-sharing demand concentrates using a four-panel dashboard.

### Dataset
`data/carshare.csv` is the **real example dataset** bundled with Plotly Express (`plotly.express.data.carshare`), originally depicting car-share demand locations in Montréal. The CSV is bundled to avoid downloading or installing Plotly.

### Approach
Create histograms, scatterplots, average usage by peak hour, and a longitude/latitude usage map-like scatter plot using Matplotlib.

### Result
Verified offline run: **249 rows** and **1,092.53 average car-hours**; four-panel figure created.

### Key Insight
The spatial view can reveal usage hot spots missed in the overall histogram: areas with similar peak times need not have similar car-hour usage.

### How to Run
`pip install -r requirements.txt` then `python main.py`. Works offline; charts are saved rather than opened.
