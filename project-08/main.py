"""Scrape a public HTML table into a cleaned CSV with graceful fallback."""
import argparse
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup

HERE = Path(__file__).parent
URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

def parse_table(html):
    """Extract first wikitable into clean column/value strings."""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("table.wikitable")
    if table is None: raise ValueError("No wikitable found")
    records = []
    headers = []
    for tr in table.select("tr"):
        th = tr.find_all("th", recursive=False)
        td = tr.find_all("td", recursive=False)
        if not headers and th:
            headers = [x.get_text(" ", strip=True) for x in th]
        if td:
            cells = [x.get_text(" ", strip=True) for x in td]
            records.append(cells)
    if not records: raise ValueError("No table data rows")
    # Wikipedia tables may have rowspans or extra headers; keep data rows
    # whose number of cells matches the modal row length.
    width = pd.Series([len(r) for r in records]).mode()[0]
    records = [r for r in records if len(r) == width]
    if len(headers) != width:
        headers = [f"column_{i+1}" for i in range(width)]
    frame = pd.DataFrame(records, columns=headers)
    for col in frame.columns:
        frame[col] = frame[col].str.replace(r"\[\d+\]", "", regex=True).str.strip()
    return frame.drop_duplicates().dropna(how="all")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    if args.offline:
        html = (HERE / "data" / "table_sample.html").read_text()
        source = "bundled sample HTML"
    else:
        try:
            r = requests.get(URL, headers={"User-Agent": "StudentEducationalScraper/1.0 (class project)"}, timeout=6)
            r.raise_for_status()
            html = r.text
            # Parse inside try so changed Wikipedia markup also falls back.
            frame = parse_table(html)
            source = URL
        except (requests.RequestException, ValueError) as error:
            print("Live table unavailable; using sample:", str(error)[:120])
            html = (HERE / "data" / "table_sample.html").read_text()
            source = "bundled sample HTML"
    if source == "bundled sample HTML":
        frame = parse_table(html)
    out = HERE / "outputs"
    out.mkdir(exist_ok=True)
    frame.to_csv(out / "clean_table.csv", index=False)
    print("Source:", source, "| Rows:", len(frame), "| Columns:", len(frame.columns))
    print(frame.head(3).to_string(index=False))
    print("Saved:", out / "clean_table.csv")

if __name__ == "__main__":
    main()
