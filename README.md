# Automated Market Research Scraper

A professional, modular web scraping system built with **Python 3.13** and **Playwright**. This project demonstrates the ability to bypass modern bot detection, handle dynamic content, and deliver clean, structured data for business intelligence.

## Key Features

* **Anti-Bot Bypass:** Implements the latest `playwright-stealth` (Object-Oriented API) to mimic human behavior and avoid IP blocking.
* **Dynamic Content Handling:** Uses Playwright to render JavaScript-heavy websites that traditional scrapers (like BeautifulSoup) cannot handle.
* **Modular Architecture:** Organized into distinct modules (`scraper`, `processor`) for high maintainability and scalability.
* **Automated Data Cleaning:** Integrated with **Pandas** to transform raw HTML data into polished Excel reports (XLSX).
* **Professional Logging:** Tracks scraping progress and errors in real-time for easier debugging.

## Tech Stack

* **Language:** Python 3.13
* **Automation:** Playwright
* **Data Analysis:** Pandas, Openpyxl
* **Environment:** Microsoft Edge (Chromium)

## Project Structure

```text
Portfolio/
├── logs/               # Log files for debugging
├── output/             # Final Excel reports
├── scraper.py          # Core scraping logic & Stealth implementation
├── processor.py        # Data cleaning & Pandas integration
├── main.py             # Entry point of the application
└── README.md
