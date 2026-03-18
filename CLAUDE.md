# CLAUDE.md - Project Mandates & Guidelines

This file contains foundational mandates for Claude when working on the **TUAI Review Scrapers** project. These instructions take precedence over general defaults.

## Project Overview

Automated pipeline for literature retrieval and screening for the **TUAI DC4** systematic review. The review focuses on **LLMs in Clinical Decision Support Systems (CDSS)**. The pipeline has three stages:

1. **Scrape** — Query PubMed via NCBI API (`main.py`, `scraper.py`)
2. **Screen** — Abstract screening via Gemini API (`screening.py`)
3. **Analyze** — Parse full-paper analysis results (`full_paper_analysis.py`)

All configuration (query, output paths, CSV columns) lives in `config.py` — that is the only file that should need editing for new searches.

## Tech Stack & Coding Standards

- **Language:** Python 3.10+
- **Style:** PEP 8. Use descriptive variable names (e.g., `pubmed_results_df` instead of `df`).
- **Type Hints:** Required on all function signatures.
- **Docstrings:** Google-style for all classes and functions.
- **Data manipulation:** `pandas` only.

## Security & Environment

- Never hardcode API keys (NCBI, Gemini). Always use `python-dotenv` and load from `.env`.
- `.env` and `outputs/` must remain in `.gitignore` — never commit them.

## Architectural Patterns

- **Pipeline integrity:** Maintain the 3-stage pipeline. New features must fit into an existing stage or be explicitly defined as a new one.
- **Data persistence:** Always export in CSV, Excel (`.xlsx`), and Joblib/Pickle for redundancy.
- **API error handling:** Use retry logic (e.g., `tenacity`) for NCBI and Gemini calls — rate limits are common.
- **Configuration:** All paths, query strings, and limits go in `config.py`. No hardcoded paths elsewhere.

## Testing & Validation

- Use `MAX_RESULTS` or a `--limit` flag when testing changes to scrapers or screening logic. Test on 5–10 papers before full execution.
- After modifying `screening.py`, verify Gemini response JSON parsing is still stable.
- If inclusion/exclusion criteria change, update the flags table in `README.md`.

## Output Files

| File | Contents |
|---|---|
| `outputs/pubmed_results.csv` / `.xlsx` / `.pkl` | Raw PubMed scrape results |
| `outputs/gemini_analysis_results.csv` / `.xlsx` / `.joblib` | Abstract screening decisions |
| `outputs/failed_pmids.txt` | PMIDs that failed during scraping |

## Key Files

| File | Purpose |
|---|---|
| `config.py` | Search query, MAX_RESULTS, output filenames, CSV columns |
| `main.py` | Entry point — runs PubMed scraping |
| `scraper.py` | `PubMedScraper` class (NCBI API logic) |
| `screening.py` | Abstract screening via `gemini-2.5-flash` |
| `full_paper_analysis.py` | Parses `---END---`-delimited JSON from NotebookLM |
| `utils.py` | Shared utilities |
