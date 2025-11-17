# Macro Meets Microchips
Over the past decade, AI has become one of the hottest sectors in the world. Companies are investing large amounts into AI infrastructure, which has created a large demand for NVIDIA products. As companies integrate more AI into their infrastructure, we expect them to replace certain jobs. Our hypothesis is that the increase in demand for NVIDIA products will lead to higher US unemployment. I am also planning to use the S&P 500 as a benchmark to measure the overall economy’s health to help with noise. 

# Data sources
| Data Source | Name/Short Description | Source/URL | Type | List of Fields | Format | Python Access? | Estimated Data Size |
|--------------|------------------------|-------------|------|----------------|---------|----------------|---------------------|
| 1 | NVIDIA Historical Stock Prices| API Call | API Call | Date, Open, High, Low, Close | API Call to CSV | Yes | 308 |
| 2 | SPY Historical Stock Prices| API Call | API Call | Date, Open, High, Low, Close | API Call to CSV | Yes | 308 |
|3 | US Unemployment Rate | API Call | API Call | Date, Unrate | API Call to CSV | Yes | 308 |


# Results 
![NVIDIA Statistical Plots](results/NVIDIA_histogram.png)
After extracting the data, I ran the function plot_statistics to create a basic histogram and line graph of each dataset. The NVIDIA and SPY Dataset had very similiar charts, as they both trend upwards. Since NVIDIA is a part of the S&P 500, we expect both of these datasets to have strong correlation. However, the S&P 500 is a better indicator of the overall US Economy Health because NVIDIA is vulnerable to many factors. When we look at the US Unemployment rate graphs, we don't see any major trends, but we do see one massive spike. This spike is related to COVID19, so I used the interpolate function to smooth out the curve. Although I want to keep everything as realistic as possible, the COVID19 pandemic is a complete outlier and is not representative of the economy health at all. We see another large spike from 2008-2012, and this is due to the Global Financial Crisis. However, this was a more natural buildup, so I kept it in our data.
ß
The correlation analysis plots tell us more about the relationships of the datasets. When we look at the NVIDIA Log Close price and US Unemployments Rate scatter plot, we can can see a clear negative correlation. This graph tells me that when NVIDIA Log Close Prife is high, US Unemployment Rate is low and vice versa. We can also see the same exact negative correlation trend with SPY Log Close Price and US Unemployment Rate. However, according to our heatmaps, SPY Log Close Price is slighly more negative correlated to US Unemployment Rate than NVIDIA. To get a better view at all three datasets, I created a line graph and heatmap with all three datasets. It shows a beter view of how all three datasets are related to each other. 

Finally, I wanted to break up the data into a Pre-AI Boom and Post-AI Boom correlation analysis. Artifical Intelligence has been a concept for a very long time, but it has become more of a reality recently. I chose the start of the AI-Boom to be December 1st, 2015, as that is when Open AI was founded. When we look at Pre-AI Boom visualizations, we actually see that NVIDIA Log Close Price and SPY Log Close Price are essentially not correlated to Unemployment. This meant that there is almost no relationship between these variables prior to the AI Boom. When we look at the Post AI-boom, we actually see that there is a moderative negative correlation between NVIDIA Log Close Price and US Unemployment Rate. Unlike my initial hypothesis, we see an increase in NVIDIA Log Stock Price and decrease in US Unemployment Rate. This means that as demand for NVIDIA increases or decreases, we will see the US Unemployment Rate move in the opposite direction. It should be noted that this is a correlation analysis and not a causation analysis, so we cannot say that changes in NVIDIA Log Stock Price cause Unemployment. However, with this analysis, we can say that there is a moderate negative relationship between the NVIDIA Log Stock Price and US Unemployment Rate. 


# Installation
- The only API key required for this project is a free FRED API Key. After creating a free account, ther user will receive an API Key. The user should set this variable 'FRED_API_KEY' to the FRED API Key in the .env file. In the project's config.py file, the user will be using the load_dotenv function from the dotenv Python package to load the API Key. This prevents the user from hard coding the API key into their code, which is very bad practice. 
- I used a handful of Python Packages. os is a Python Package that allows users to navigate through files and directories. I use it to navigate through files and directories, as well as create directories if they do not exist. I use Pandas and Numpy as powerful data analysis tools. Pandas allowed me to easily parse, clean, edit, and filter data, while Numpy allowed me to make log operation compputations easily. yfinance is a Python Package that allowed me to obtain historical market data from Yahoo Finance. I used yfinance to obtain my SPY and NVIDIA stock data. fredapi is a Python wrapper, which I used to retrive data from the Federal Reserve Economic Data (FRED) using an API Key and special parameters. Finally. I used seaborn and matplotlib as my main tools for data visualization. I used seaborn to make simple statistical plots, and I used matplotlib to help with titles/labels.

# Running analysis 
Create free FRED account and obtain API Key. Create API_FRED_KEY and set the API Key in the .env file 

From `src/` directory run:

`python main`

Results will appear in `results/` folder.