## 🤖 ml-crawlers-lab Repository
A comprehensive collection of Python practice projects focused on web crawling, data automation, AI integration, data analysis, and visualization.
This repository includes modular examples demonstrating real-world applications such as scraping popular websites, processing stock and financial data, integrating OpenAI, and analyzing datasets using pandas and matplotlib.

## 🛠 Technologies Used
Python 3.x

Web Crawling: Selenium, BeautifulSoup, requests

Automation & Scheduling: time, threading, os

Data Handling: json, dotenv, pandas, openpyxl

Visualization: matplotlib

AI & LLMs: openai, LangChain

Excel & Image Processing: Pillow (PIL), xlsxwriter

## 📌 Key Topics Covered
📦 Amazon Website Crawler
Extract product and context data from Amazon using requests and HTML parsing.

📸 Instagram User Info Crawler
Automate login and extract user content with environment variables for secure auth.

🟢 Naver Auto Login & Blog Crawler
Automate login, handle CAPTCHA, and scrape blog content using scrolling logic.

🪙 CoinOne Cryptocurrency Price Crawler
Real-time price scraping and storage in JSON.

📈 Korea Stock Price Crawler
Scrape and parse South Korean stock market data with multi-threaded logic.

🧵 Multithreading Practice
Apply threading to speed up crawling and reduce blocking I/O time.

🧠 OpenAI Vision & Text Integration
Use gpt-4, dall-e, and vision APIs to analyze images and generate text.

📊 Data Analysis with Pandas
Clean, group, and analyze data with pandas and visualize with matplotlib.

🧮 Regression Analysis
From basic linear regression to advanced model comparison using datasets.

🧱 Object-Oriented Programming
Class structure and object management examples (CreateObject.py).

📁 File I/O and Management
Read/write handling for .txt, .json, .xlsx and directory ops.

🖼 Image Resizing Automation
Process and resize images using the PIL library.

⏱ Time-Based Execution & Control
Scripts using time.sleep(), timing execution, or simulating delays.

## 📂 Project Structure
```
Python-Study-Repository/
│
├── Ai/                                      # OpenAI API and translation-related scripts
│   ├── .env
│   ├── english.xlsx                         # Input Excel file for translation
│   ├── OpenAi_img.py                        # OpenAI Vision API (image-to-text)
│   ├── OpenAi_text.py                       # OpenAI Text API usage
│   ├── output.xlsx                          # Output Excel file with translated results
│   ├── test.jpg                             # Test image for Vision API
│   ├── Translate_exel.py                    # Excel translation handler
│   ├── Translate_http.py                    # HTTP-based translation script
│   └── Translate.py                         # General-purpose translation logic
│
├── Langchain/                               # LangChain-based LLM experiment scripts
│   └── Langchain_1.py                       # Sample test using LangChain + ChatModel
│
├── Pandas/                                  # Data analysis using pandas
│   ├── credit.csv                           # Sample dataset
│   ├── Pandas_1.py                          # Basic DataFrame operations
│   ├── Pandas_2.py                          # Grouping and aggregation
│   ├── Pandas_3.py                          # Cleaning and filtering
│   ├── PandasAnalyze.py                     # Custom analysis logic
│   └── product.xlsx                         # Excel-based product dataset
│
├── Visualization/                           # Data visualization and regression analysis
│   ├── california_housing.csv               # Dataset for regression examples
│   ├── income.txt                           # Example dataset (income)
│   ├── matplot_Graph.py                     # Graph drawing using matplotlib
│   ├── regression_analysis_1.py             # Basic linear regression analysis
│   ├── regression_analysis_2.py             # Multiple regression
│   ├── regression_analysis_3.py             # Regression using scikit-learn
│   ├── regression_analysis_4.py             # Comparison of regression metrics (R², MSE)
│   ├── regression_analysis_5.py             # Comparing different regression models
│   └── StockData.py                         # Regression visualization on stock data
│
├── WebCrawler/                              # Web scraping scripts by target site
│   ├── Amazon/
│   │   ├── WebContext.txt                   # Crawler context or notes
│   │   └── WebsiteCrawle.py                 # Amazon crawler
│   │
│   ├── Instagram/
│   │   ├── .env
│   │   ├── .gitignore
│   │   └── InstagramCrawle.py               # Instagram user data crawler
│   │
│   ├── Naver/
│   │   ├── .env
│   │   ├── .gitignore
│   │   ├── BlogScrollCrawler.py             # Naver blog scroll crawler
│   │   └── Logincaptcha.py                  # Login + CAPTCHA automation
│   │
│   └── Stock/
│       ├── CoinCrawler.py                   # Coin market crawler
│       ├── CrawlerResult.txt                # Example output of crawling
│       ├── MultiThread.py                   # Web crawling using multithreading
│       ├── project.py                       # Stock crawling project entry
│       ├── StockCrawler.py                  # Stock data crawler
│       ├── test.json                        # Sample output in JSON format
│       └── WebCrawler.py                    # General-purpose web crawler
│
├── Others/                                  # Miscellaneous files
│
├── testFile/                                # Temporary test scripts or data
├── testFile2/                               # Another test directory
│
├── CreateObject.py                          # Object-oriented programming example
├── FileControll.py                          # File read/write control
├── ImageResizing.py                         # Image resize operations
├── TimeProcess.py                           # Script demonstrating time-related operations
│
├── .gitignore
└── README.md


```
## 📃 License
This project is open for educational and personal use. No specific license is applied.
