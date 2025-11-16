# Macro Meets Microchips
Over the past decade, AI has become one of the hottest sectors in the world. Companies are investing large amounts into AI infrastructure, which has created a large demand for NVIDIA products. As companies integrate more AI into their infrastructure, we expect them to replace certain jobs. Our hypothesis is that the increase in demand for NVIDIA products will lead to higher US unemployment. I am also planning to use the S&P 500 as a benchmark to measure the overall economy’s health to help with noise. 

# Data sources
| Data Source | Name/Short Description | Source/URL | Type | List of Fields | Format | Python Access? | Estimated Data Size |
|--------------|------------------------|-------------|------|----------------|---------|----------------|---------------------|
| 1 | NVIDIA Historical Stock Prices| API Call | API Call | Date, Open, High, Low, Close | API Call to CSV | Yes | 308 |
| 2 | SPY Historical Stock Prices| API Call | API Call | Date, Open, High, Low, Close | API Call to CSV | Yes | 308 |
|3 | US Unemployment Rate | API Call | API Call | Date, Unrate | API Call to CSV | Yes | 308 |


# Results 
_describe your findings_

# Installation
- The only API key required for this project is a free FRED API Key. After creating a free account, ther user will receive an API Key. The user should set this variable 'FRED_API_KEY' to the FRED API Key in the .env file. In the project's config.py file, the user will be using the load_dotenv function from the dotenv Python package to load the API Key. This prevents the user from hard coding the API key into their code, which is very bad practice. 
- I used a handful of Python Packages. os is a Python Package that allows users to navigate through files and directories. I use it to navigate through files and directories, as well as create directories if they do not exist. I use Pandas and Numpy as powerful data analysis tools. Pandas allowed me to easily parse, clean, edit, and filter data, while Numpy allowed me to make log operation compputations easily. yfinance is a Python Package that allowed me to obtain historical market data from Yahoo Finance. I used yfinance to obtain my SPY and NVIDIA stock data. fredapi is a Python wrapper, which I used to retrive data from the Federal Reserve Economic Data (FRED) using an API Key and special parameters. Finally. I used seaborn and matplotlib as my main tools for data visualization. I used seaborn to make simple statistical plots, and I used matplotlib to help with titles/labels.

# Running analysis 
_update these instructions_


From `src/` directory run:

`python main`

Results will appear in `results/` folder. All obtained will be stored in `data/`