"""Cluster countries by GDP, life expectancy and population.

Use World Bank API if available; otherwise the bundled Gapminder snapshot.
"""
import argparse
from pathlib import Path
import pandas as pd
import requests
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

HERE = Path(__file__).parent
COUNTRY_CODES = {"IN": "India", "CN": "China", "US": "United States",
                 "DE": "Germany", "BR": "Brazil", "JP": "Japan",
                 "ZA": "South Africa", "MX": "Mexico", "NG": "Nigeria",
                 "ID": "Indonesia", "NO": "Norway", "BD": "Bangladesh"}
INDICATORS = {"NY.GDP.PCAP.CD": "gdp_per_capita_usd",
              "SP.DYN.LE00.IN": "life_expectancy",
              "SP.POP.TOTL": "population"}

def fetch_world_bank():
    """Request three indicators, using the latest available values by country."""
    rows = {name: {"country": name} for name in COUNTRY_CODES.values()}
    codes = ";".join(COUNTRY_CODES)
    for indicator, column in INDICATORS.items():
        url = f"https://api.worldbank.org/v2/country/{codes}/indicator/{indicator}"
        response = requests.get(url, params={"format": "json", "per_page": 1500}, timeout=5)
        response.raise_for_status()
        records = response.json()[1]
        if not records:
            raise ValueError("World Bank returned no rows")
        for item in records:
            name = item.get("country", {}).get("value")
            if name in rows and item["value"] is not None and column not in rows[name]:
                rows[name][column] = float(item["value"])
    table = pd.DataFrame(rows.values()).dropna()
    if len(table) < 6:
        raise ValueError("Not enough complete live countries")
    return table

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Use bundled real Gapminder snapshot")
    args = parser.parse_args()
    if args.offline:
        data = pd.read_csv(HERE / "data" / "gapminder_2007.csv")
        source = "Gapminder 2007 (bundled)"
    else:
        try:
            data = fetch_world_bank()
            source = "World Bank API (latest per indicator)"
        except (requests.RequestException, ValueError, IndexError, KeyError, TypeError) as error:
            print("API unavailable; using bundled data:", str(error)[:100])
            data = pd.read_csv(HERE / "data" / "gapminder_2007.csv")
            source = "Gapminder 2007 (bundled)"
    columns = ["gdp_per_capita_usd", "life_expectancy", "population"]
    # Log-transform highly skewed GDP and population before standardizing.
    import numpy as np
    transformed = data[columns].copy()
    transformed["gdp_per_capita_usd"] = np.log1p(transformed["gdp_per_capita_usd"])
    transformed["population"] = np.log1p(transformed["population"])
    scaled = StandardScaler().fit_transform(transformed)
    data["cluster"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(scaled)
    print("Source:", source)
    print(data[["country", "cluster", "life_expectancy"]].sort_values("cluster").to_string(index=False))
    print("Mean life expectancy by cluster:")
    print(data.groupby("cluster")["life_expectancy"].mean().round(1).to_string())

if __name__ == "__main__":
    main()
