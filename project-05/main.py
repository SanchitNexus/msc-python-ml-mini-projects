"""Visualize car-sharing usage with four charts from an actual sample dataset."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent

def main():
    df = pd.read_csv(HERE / "data" / "carshare.csv")
    output = HERE / "outputs"
    output.mkdir(exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    axes[0, 0].hist(df["car_hours"], bins=18)
    axes[0, 0].set_title("Distribution of car-hours")
    axes[0, 1].scatter(df["peak_hour"], df["car_hours"], alpha=0.6)
    axes[0, 1].set_title("Peak hour vs car-hours")
    axes[1, 0].bar(df.groupby("peak_hour")["car_hours"].mean().index,
                   df.groupby("peak_hour")["car_hours"].mean().values)
    axes[1, 0].set_title("Mean car-hours by peak hour")
    axes[1, 1].scatter(df["centroid_lon"], df["centroid_lat"], c=df["car_hours"], cmap="viridis")
    axes[1, 1].set_title("Locations colored by car-hours")
    for ax in axes.flat: ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(output / "dashboard.png", dpi=140)
    plt.close(fig)
    print("Rows:", len(df), "| Average car-hours:", round(df["car_hours"].mean(), 2))
    print("Saved:", output / "dashboard.png")

if __name__ == "__main__":
    main()
