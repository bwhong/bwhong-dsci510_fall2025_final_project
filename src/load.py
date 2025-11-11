import os
import pandas as pd
import yfinance as yf
from fredapi import Fred

# --- 1. Extract Data FROM FRED ---

def get_fred_data(dataset, observation_start_date, observation_end_date, api_key, freq= 'm'):
    """
    Downloads a specific file from FRED, extracts it,
    and loads it into a pandas DataFrame.

    :param dataset: Dataset to extract
    :param observation_start: Observation Start Date
    :param observation_end: Observation End Date
    :param api_key_file: API Key File
    :param freq: Frequency of Data
    :return: pandas DataFrame or None
    """
    print(f"--- Extracting data from FRED: {dataset} ---")
    try:
        print(f"Extracting {dataset}...")
        fred = Fred(api_key = api_key)
        data = fred.get_series(
                series_id= dataset,           
                observation_start= observation_start_date, 
                observation_end=observation_end_date,   
                frequency= freq                       
                )
        data = data.reset_index()
        data.columns = ['Date', 'Value']
        data['Date'] = pd.to_datetime(data['Date'])
        return data
    except Exception as e:
        print(f"Error loading data from FRED: {e}")
        return None
    
# --- 2. Exract Data from yfinance ---

def get_stock_data(dataset, observation_start_date, observation_end_date, interval, auto_adjust = True):
    """
    Extract a specific file from yfinance, extracts it,
    and loads it into a pandas DataFrame.

    :param dataset: Dataset to extract
    :param observation_start: Observation Start Date
    :param observation_end: Observation End Date
    :param interval: Frequency of Data
    :param auto_adjust: Boolean that controls whether the price data is adjusted for stock splits and dividends. By Default, I have set it to True.
    :return: pandas DataFrame or None
    """
    print(f"--- Loading data from yfinance: {dataset} ---")
    try:
        print(f"Extracting {dataset}...")
        data = yf.download(
            tickers = dataset, 
            start = observation_start_date,
            end = observation_end_date,
            interval = interval,
            auto_adjust= auto_adjust                  
            )
        data = data.reset_index()[['Date', 'Close']]
        data['Date'] = pd.to_datetime(data['Date'])
        data['Close'] = data['Close'].pct_change()
        return data
    except Exception as e:
        print(f"Error loading data from yfinance: {e}")
        return None