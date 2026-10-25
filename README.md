# 10 Python & ML Mini-Projects — M.Sc. Informatics Lab

**Author:** Sanchit Kumar Mishra  
**Program:** M.Sc. Informatics — University of Delhi (South Campus)  

Ten independently runnable, beginner-readable mini-projects. **Three use free keyless APIs:** project-03 (World Bank), project-06 (Open-Meteo), project-07 (Open Library). All other projects are offline; project-08 optionally scrapes a live Wikipedia HTML table. No excluded datasets/topics were used.

## Projects

| Folder | Focus | Data | API? |
|---|---|---|---|
| project-01 | MPG regression | Bundled synthetic vehicle specs | No |
| project-02 | Wine classification | sklearn wine (built in) | No |
| project-03 | Country clustering | World Bank / bundled Gapminder 2007 | **Yes** |
| project-04 | Spam NLP | Bundled synthetic SMS | No |
| project-05 | Multi-panel visualization | Bundled Plotly car-sharing example | No |
| project-06 | Temperature moving average | Open-Meteo / bundled El Niño historical data | **Yes** |
| project-07 | Book tag recommendation | Open Library / bundled curated catalog | **Yes** |
| project-08 | HTML table scraping | Wikipedia / bundled HTML fallback | No (scraping) |
| project-09 | Duplicate file automation | Bundled example files / own directory | No |
| project-10 | Macroeconomic EDA | Bundled statsmodels macrodata | No |

## Quick start

Use Python 3.10+ and run a project **from any current working directory**:

```bash
cd project-01
python -m pip install -r requirements.txt
python main.py
```

Repeat for each folder. The three API-based projects support `python main.py --offline`; project-08 also supports `--offline`. Project-09 requires no packages. Output files are saved in project-local `outputs/` folders (gitignored).

## Test all 10

Create an environment with `python -m pip install -r requirements-all.txt`, then run `python test_all.py`. This executes all 10 scripts from the repository root using offline mode where applicable and verifies their exit codes. It also checks specific output artifacts. A successful offline test does **not** prove that a remote API is reachable from every network; each live attempt has an automatic fallback.

## Publish on GitHub

```bash
git init
git add .
git commit -m "Add ten tested MSc Informatics Python mini-projects"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/msc-python-ml-mini-projects.git
git push -u origin main
```

Create an empty GitHub repository with this name first and replace `YOUR_USERNAME`. These instructions do not publish automatically: they require your GitHub account authorization.

## Class demonstration

For each project: state the input data source; explain the 3–5 processing steps; run `main.py`; show the printed result/chart; end with the `Key Insight` plus one limitation. Small or synthetic datasets are intentionally disclosed in each README rather than described as real benchmarks.
