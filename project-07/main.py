"""Recommend books by textual similarity of genre and subject tags."""
import argparse
from pathlib import Path
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

HERE = Path(__file__).parent

def fetch_books():
    """Get public-domain book titles and subjects from Open Library."""
    response = requests.get("https://openlibrary.org/subjects/fiction.json",
                            params={"limit": 35}, timeout=6)
    response.raise_for_status()
    books = []
    for entry in response.json().get("works", []):
        subjects = entry.get("subject", [])
        tags = " ".join(str(s).replace("_", " ") for s in subjects[:15])
        if entry.get("title") and tags:
            books.append({"title": entry["title"], "tags": tags})
    if len(books) < 5:
        raise ValueError("Not enough tagged books returned")
    return pd.DataFrame(books).drop_duplicates("title").reset_index(drop=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--title", default=None, help="A book title shown in the list")
    args = parser.parse_args()
    if args.offline:
        books = pd.read_csv(HERE / "data" / "books.csv")
        source = "bundled teaching catalog"
    else:
        try:
            books = fetch_books()
            source = "Open Library Subjects API"
        except (requests.RequestException, ValueError, KeyError, TypeError) as error:
            print("API unavailable; using bundled catalog:", str(error)[:100])
            books = pd.read_csv(HERE / "data" / "books.csv")
            source = "bundled teaching catalog"
    vector = TfidfVectorizer(stop_words="english").fit_transform(books["tags"].fillna(""))
    scores = cosine_similarity(vector)
    selected = args.title or books.iloc[0]["title"]
    matches = books.index[books["title"].str.lower() == selected.lower()].tolist()
    if not matches:
        print("Unknown title. Available examples:", ", ".join(books["title"].head(8)))
        selected_index = 0
    else:
        selected_index = matches[0]
    neighbors = sorted(enumerate(scores[selected_index]), key=lambda x: x[1], reverse=True)
    print("Source:", source, "| Selected:", books.iloc[selected_index]["title"])
    for i, score in [item for item in neighbors if item[0] != selected_index and item[1] > 0][:5]:
        print(f"{books.iloc[i]['title']} | similarity {score:.3f}")

if __name__ == "__main__":
    main()
