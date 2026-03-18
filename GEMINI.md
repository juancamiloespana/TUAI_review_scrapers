# GEMINI.md - Project Mandates & Guidelines

This file contains foundational mandates for Gemini CLI when working on the **TUAI Review Scrapers** project. These instructions take precedence over general defaults.

## 🛠 Tech Stack & Coding Standards
- **Language:** Python 3.10+
- **Style:** Adhere to PEP 8. Use descriptive variable names (e.g., `pubmed_results_df` instead of `df`).
- **Type Hinting:** Use Python type hints for all function signatures.
- **Documentation:** Use Google-style docstrings for all classes and functions.

## 🔒 Security & Environment
- **Secrets:** Never hardcode API keys (NCBI, Gemini). Always use `python-dotenv` and load from `.env`.
- **Git:** Ensure `.env` and `outputs/` are in `.gitignore`.

## 🏗 Architectural Patterns
- **Pipeline Stages:** Maintain the 3-stage pipeline (Scrape -> Screen -> Analyze). New features should fit into one of these or be clearly defined as a new stage.
- **Data Persistence:** 
    - Always export data in multiple formats for redundancy: CSV, Excel (`.xlsx`), and Joblib/Pickle for internal state.
    - Use `pandas` for data manipulation.
- **Error Handling:** Implement robust retry logic for API calls (NCBI, Gemini) using `tenacity` or similar patterns, as rate limits are common.

## 🧪 Testing & Validation
- **Dry Runs:** When modifying scrapers or screening logic, always implement a `--limit` or `MAX_RESULTS` flag to test on a small subset (e.g., 5-10 papers) before full execution.
- **Verification:** After modifying `screening.py`, verify that the JSON parsing of Gemini responses remains stable.

---

## 💡 Examples of how GEMINI.md works

### Example 1: Creating a new scraper
**Requirement:** If asked to add an "Arxiv" scraper.
**GEMINI.md Impact:** I must:
1. Use `python-dotenv` for any Arxiv API keys.
2. Ensure it outputs CSV, Excel, and Joblib files.
3. Add type hints and Google-style docstrings.
4. Add a `MAX_RESULTS` config in `config.py`.

### Example 2: Modifying screening logic
**Requirement:** Change the inclusion criteria.
**GEMINI.md Impact:** I must:
1. Update `screening.py`.
2. Run a "Dry Run" with 5 papers to verify the Gemini API still returns correctly formatted JSON.
3. Update the `README.md` table of exclusion flags if they changed.

### Example 3: Refactoring `main.py`
**Requirement:** Clean up the main entry point.
**GEMINI.md Impact:** I must maintain the PEP 8 style and ensure no hardcoded paths are introduced (use `config.py`).
