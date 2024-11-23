# 🏘️ FB Group Crawler

## 📌 Overview

A tool that can automatically crawl post content from **Facebook groups**. This tool uses Selenium to automate Facebook login and navigation, extracting post information from specified Facebook groups, including the author, post time, and content, and saving the results as JSON files.

---

## 📌 Features

- Automatically log in to Facebook, access specified groups, and scrape the day's posts in chronological order.
- Extract post **author**, **post time**, and **post content**.
- Save the results as JSON files for later review.

---

## 📌 Workflow

1. **Set Facebook Account and Password**: Configure your Facebook account and password in the `.env` file.
2. **Run the Crawler Script**: Execute `crawler.py` to automate Facebook login and begin scraping group posts.
3. **Save Results**: The scraped posts will be saved as JSON files, organized by the storage date.

---

## 📌 Environment Setup and Running Scripts

### 1. **Environment Setup**

* Ensure Python 3 or above is installed on your system.
* Install the required Python packages:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include the following packages:

* Selenium
* Python-dotenv
* Webdriver-manager

### 2. **Run the Crawler Script**

Run the following command to start the crawler tool:

```bash
python crawler.py
```

### 3. **Notes**

* Ensure that the `input.txt` file contains the Facebook group links you want to scrape (one link per line).
* Make sure your Facebook account can log in successfully and that the groups are visible.

---

## 📌 File Structure

```
project/
├── crawler.py    # Main crawler script
└── input.txt     # File containing group links
```

---

## 📌 Error Handling

* If unable to log in to Facebook, check if the account and password in the `.env` file are correct.
* If a page cannot be loaded or elements cannot be found, it might be due to network issues or Facebook page updates. The program will skip that post and continue.

---

## 📌 Version Information

### v1.0

Current version (v1.0) includes:

* Basic functionality to log in to Facebook and scrape group posts.
* Error handling and page scrolling to fetch more posts.

