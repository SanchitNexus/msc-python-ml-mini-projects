"""Generate numeric summaries, missingness, outliers and correlation plot."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent

def main():
    df = pd.read_csv(HERE / "data" / "macrodata.csv")
    numeric = df.select_dtypes(include="number")
    missing = df.isna().sum()
    q1 = numeric.quantile(0.25)
    q3 = numeric.quantile(0.75)
    iqr = q3 - q1
    outliers = ((numeric < q1 - 1.5 * iqr) | (numeric > q3 + 1.5 * iqr)).sum()
    folder = HERE / "outputs"
    folder.mkdir(exist_ok=True)
    numeric.describe().round(2).to_csv(folder / "summary.csv")
    missing.to_csv(folder / "missing.csv", header=["missing_count"])
    outliers.to_csv(folder / "outliers.csv", header=["iqr_outliers"])
    correlation = numeric.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    image = ax.imshow(correlation.values, vmin=-1, vmax=1, cmap="coolwarm")
    ax.set_xticks(range(len(correlation.columns)), labels=correlation.columns, rotation=90)
    ax.set_yticks(range(len(correlation.columns)), labels=correlation.columns)
    fig.colorbar(image, ax=ax, label="Pearson r")
    fig.tight_layout()
    fig.savefig(folder / "correlation.png", dpi=130)
    plt.close(fig)
    print("Rows:", len(df), "| Columns:", len(df.columns))
    print("Missing values total:", int(missing.sum()))
    print("Most IQR outliers:", outliers.sort_values(ascending=False).head(3).to_dict())
    print("Saved reports in", folder)

if __name__ == "__main__":
    main()
