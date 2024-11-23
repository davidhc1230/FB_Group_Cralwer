# 🏘️ FB 社團爬蟲工具

## 📌 概述

一個能夠自動從 **Facebook 社團** 中爬取貼文內容的工具。此工具使用 Selenium 自動化 Facebook 的登入和瀏覽，從指定的 Facebook 社團中擷取貼文資訊，包括發文者、發文時間以及內文，並將結果保存為 JSON 文件。

---

## 📌 功能

- 自動登入 Facebook，進入指定社團，按時間順序爬取當日貼文。
- 爬取貼文的 **發文者**、**發文時間** 及 **貼文內容**。
- 將結果保存為 JSON 文件，以便後續查閱。

---

## 📌 運作流程

1. **設定 Facebook 帳號與密碼**：在 `.env` 文件中設定您的 Facebook 帳號與密碼。
2. **啟動爬蟲腳本**：執行 `crawler.py`，自動化登入 Facebook，並開始爬取社團貼文。
3. **結果保存**：爬取的貼文將依儲存日期保存為 JSON 文件。

---

## 📌 環境設定及運行腳本

### 1. **環境設定**

- 確保系統已安裝 Python 3 或以上版本。
- 安裝所需的 Python 套件：

```bash
pip install -r requirements.txt
```

`requirements.txt` 應包含以下套件：

- Selenium
- Python-dotenv
- Webdriver-manager

### 2. **運行爬蟲腳本**

執行以下指令啟動爬蟲工具：

```bash
python crawler.py
```

### 3. **注意事項**

- 確保 `input.txt` 文件中包含您希望爬取的 Facebook 社團連結（每行一個連結）。
- 請確認您的 Facebook 帳號可以成功登入，並且已加入社團。

---

## 📌 檔案結構

```
project/
├── crawler.py    # 主爬蟲程式
└── input.txt              # 包含社團連結的文件
```

---

## 📌 錯誤處理

- 若無法登入 Facebook，請檢查 `.env` 中的帳號與密碼是否正確。
- 當頁面無法載入或元素找不到時，可能是由於網路問題或 Facebook 頁面更新，程式會跳過該貼文並繼續。

---

## 📌 版本資訊

### v1.0

目前的版本（v1.0）包括：

- 自動化登入 Facebook 並爬取社團貼文的基本功能。
- 錯誤處理和頁面滾動以獲取更多貼文。

