## Wine Cultivar Classification

### Problem Statement
Predict the cultivar of wine from its chemical measurements, without using flowers or medical data.

### Dataset
`sklearn.datasets.load_wine`, a built-in public benchmark with 178 samples, 13 features and 3 cultivars (source: UCI Wine dataset).

### Approach
Stratified 75/25 split; standardize numeric features; fit 5-nearest-neighbors; inspect accuracy and confusion matrix.

### Result
Verified offline test: accuracy **0.933** (42/45 correct on held-out wine samples).

### Key Insight
Wine chemistry features have different numerical scales, so scaling is essential for distance-based KNN: without it, high-magnitude measurements can dominate the neighbor search.

### How to Run
`pip install -r requirements.txt` then `python main.py`. Works offline.
