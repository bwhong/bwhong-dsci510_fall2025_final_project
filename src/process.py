import os
import pandas as pd

def process_fred_data(data, primary_column_name):
    """
    Process FRED Data. Change column names to a clean name. Change Date Column to datetime data type.

    :param dataset: Dataset to process
    :param primary_column_name: Primary Column Name to replace Value
    :return: pandas DataFrame or None
    """
    print(f"--- Processing {primary_column_name} Dataset")
    try:
        print(f"Processing {primary_column_name}")
        data = data.reset_index()
        data.columns = ['Date', primary_column_name]
        data['Date'] = pd.to_datetime(data['Date'])
        return data
    except Exception as e:
        print(f"Error processing {primary_column_name} data: {e}")
        return None

def process_stock_data(data, stock_name):
    """
    Process stock data. Select date and close columns. Choose first level from multi-index.
    Rename column names to a clean name. Change date column to datetime data type. Convert 
    Close Columns to percent change. 

    :param dataset: Dataset to extract
    :param stock_name: Stock Name
    :return: pandas DataFrame or None
    """
    print(f"--- Processing {stock_name} data---")
    try:
        print(f"Processing {stock_name}...")
        data = data.reset_index()[['Date', 'Close']]
        #remove multi-index and column index name
        data.columns = data.columns.get_level_values(0).rename(None)
        data['Date'] = pd.to_datetime(data['Date'])
        data['Close % Change'] = data['Close'].pct_change() * 100
        data = data[['Date', 'Close % Change']]
        data = data.dropna()
        return data
    except Exception as e:
        print(f"Error processing {stock_name} data: {e}")
        return None