"""Monthly temperature trend, 3-month moving average, and naive forecast."""
import argparse
from pathlib import Path
import pandas as pd
import requests
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent

def api_data():
    """Load historical monthly temperatures for Delhi from the free archive API."""
    url = "https://archive-api.open-meteo.com/v1/archive"
    response = requests.get(url, params={
        "latitude": 28.61, "longitude": 77.21,
        "start_date": "2022-01-01", "end_date": "2024-12-31",
        "daily": "temperature_2m_mean", "timezone": "Asia/Kolkata"
    }, timeout=6)
    response.raise_for_status()
    daily = response.json()["daily"]
    series = pd.DataFrame({"month": pd.to_datetime(daily["time"]),
                           "temperature_c": daily["temperature_2m_mean"]})
    return series.set_index("month").resample("MS").mean().dropna().reset_index()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    if args.offline:
        df = pd.read_csv(HERE / "data" / "elnino_monthly.csv", parse_dates=["month"])
        source = "El Niño Pacific temperatures, bundled"
    else:
        try:
            df = api_data()
            if len(df) < 6: raise ValueError("Too few months")
            source = "Open-Meteo historical daily temperature, Delhi"
        except (requests.RequestException, ValueError, KeyError, TypeError) as error:
            print("API unavailable; using bundled data:", str(error)[:100])
            df = pd.read_csv(HERE / "data" / "elnino_monthly.csv", parse_dates=["month"])
            source = "El Niño Pacific temperatures, bundled"
    df["moving_average_3m"] = df["temperature_c"].rolling(3).mean()
    next_forecast = df["temperature_c"].tail(3).mean()
    folder = HERE / "outputs"
    folder.mkdir(exist_ok=True)
    plt.figure(figsize=(9, 4))
    plt.plot(df["month"], df["temperature_c"], label="Monthly mean")
    plt.plot(df["month"], df["moving_average_3m"], label="3-month MA")
    plt.legend()
    plt.ylabel("Temperature (°C)")
    plt.title(source)
    plt.tight_layout()
    plt.savefig(folder / "trend.png", dpi=140)
    plt.close()
    print("Source:", source)
    print(f"One-step forecast (last 3-month mean): {next_forecast:.2f} °C")
    print("Saved:", folder / "trend.png")

if __name__ == "__main__":
    main()
