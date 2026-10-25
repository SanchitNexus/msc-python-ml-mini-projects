"""Predict fuel economy from numeric engine/vehicle specifications."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

DATA = Path(__file__).parent / "data" / "vehicles.csv"

def main():
    cars = pd.read_csv(DATA)
    features = ["cylinders", "displacement_l", "horsepower", "weight_lb"]
    x_train, x_test, y_train, y_test = train_test_split(
        cars[features], cars["mpg"], test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(f"Rows: {len(cars)} | Test MAE: {mean_absolute_error(y_test, predictions):.2f} MPG")
    print(f"Test R²: {r2_score(y_test, predictions):.3f}")
    for name, value in zip(features, model.coef_):
        print(f"Coefficient for {name}: {value:.4f}")
    print("Prediction for first test vehicle:", round(predictions[0], 1), "MPG")

if __name__ == "__main__":
    main()
