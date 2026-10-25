## Engine Specifications to MPG Prediction

### Problem Statement
Estimate vehicle MPG using cylinders, engine displacement, horsepower and vehicle weight.

### Dataset
`data/vehicles.csv` contains 260 **synthetic teaching examples** created with a fixed random seed. Units are liters, hp, pounds and MPG. These are not measurements of actual cars; do not treat the result as real-world validation.

### Approach
Split rows 80/20; fit multiple linear regression; evaluate held-out MAE and R². Print model coefficients to discuss feature effects.

### Result
Verified offline test: MAE **1.98 MPG**, R² **0.893** (synthetic held-out data).

### Key Insight
Because the sample generator makes heavier, higher-horsepower vehicles consume more fuel, vehicle weight and horsepower jointly explain much of the apparent MPG variation; this association is built into the synthetic data and is not a causal discovery.

### How to Run
`pip install -r requirements.txt` then `python main.py`. Works offline.
