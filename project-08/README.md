## Wikipedia Table Scraper with Offline HTML Fallback

### Problem Statement
Automatically convert an HTML table into an analyzable CSV.

### Dataset
The public [Wikipedia list of countries and dependencies by population](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population) (web page, **not** one of the three API projects). Bundled `data/table_sample.html` contains five manually supplied country/capital rows solely to guarantee offline execution; live and fallback tables have **different schemas**.

### Approach
`requests` downloads HTML; BeautifulSoup finds a `wikitable`, extracts headers and cells, normalizes citation markers, and pandas saves a CSV. Fallback on network/markup failure.

### Result
Verified offline run: **5 rows × 2 columns** parsed and saved from bundled sample HTML.

### Key Insight
A web table is presentation-oriented, not analysis-ready: merged cells, footnote markers and changing markup can alter columns and row counts, so a scraper must validate the extracted structure.

### How to Run
`pip install -r requirements.txt` then `python main.py`, or `python main.py --offline` for reliable classroom use. Respect the website's usage policy and avoid repeated rapid requests.
