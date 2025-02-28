# Web Scraping Project

![Web Scraping](https://img.shields.io/badge/Web%20Scraping-Python-blue.svg)

## 📌 Project Overview
This repository contains various web scraping scripts designed to extract data from multiple websites. The scripts leverage Python libraries such as `Scrapy`, `BeautifulSoup`, and `Selenium` to scrape and collect structured data efficiently. The collected data can be utilized for analysis, visualization, or further machine learning applications.

## 🚀 Features
- Extracts data from websites dynamically and efficiently.
- Supports multiple web scraping techniques:
  - Static scraping using `requests` and `BeautifulSoup`.
  - Dynamic scraping using `Selenium`.
  - Scalable scraping with `Scrapy`.
- Saves data in structured formats such as CSV, JSON, and databases.
- Handles pagination, AJAX content, and authentication-based scraping.

## 🛠 Tech Stack
- **Programming Language:** Python
- **Libraries:**
  - `BeautifulSoup`
  - `Scrapy`
  - `Selenium`
  - `Requests`
  - `Pandas`
  - `Lxml`
- **Storage Formats:** CSV, JSON, SQLite


## 🔧 Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/SimranShaikh20/WebScraping.git
   cd WebScraping
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```


## 📌 How to Use
### 1. Running BeautifulSoup Scraper
```bash
python scripts/beautifulsoup_scraper.py
```
### 2. Running Selenium Scraper
```bash
python scripts/selenium_scraper.py
```
### 3. Running Scrapy Spider
```bash
cd scripts/scrapy_project
scrapy crawl spider_name -o output.json
```

## 📝 Example Output
```json
[
  {
    "title": "Sample Job Post",
    "company": "Tech Corp",
    "location": "New York, USA",
    "salary": "$80,000 - $100,000"
  }
]
```

## 📬 Contact
For any queries or contributions, feel free to reach out:
- **GitHub:** [SimranShaikh20](https://github.com/SimranShaikh20)


## ⭐ Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

---
**Happy Scraping! 🕷️**
