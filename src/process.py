import pandas as pd
import numpy as np

def process_fred_data(data, primary_column_name, covid = False):
    """
    Process FRED Data. Change column names to a clean name. Change Date Column to datetime data type.

    :param dataset: Dataset to process
    :param primary_column_name: Primary Column Name to replace Value
    :return: pandas DataFrame or None
    """
    print(f"--- Processing {primary_column_name} Dataset")
    try:
        print(f"Processing {primary_column_name}")
        #reset index and select rename column names
        data = data.reset_index()
        data.columns = ['Date', primary_column_name]
        #convert to datetime
        data['Date'] = pd.to_datetime(data['Date'])
        #standaridze covid data
        if covid:
            #covid start and end dates declared by World Health Organization(WHO)
            covid_dates = (data['Date'] >= '2020-03-01') & (data['Date'] <= '2023-05-01')
            data.loc[covid_dates, primary_column_name] = np.nan
            data[primary_column_name] = data[primary_column_name].interpolate(method='linear')
        return data
    except Exception as e:
        print(f"Error processing {primary_column_name} data: {e}")
        return None

def process_stock_data(data, stock_name, log = True):
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
        #reset index
        data = data.reset_index()
        #remove multi-index and column index name
        data.columns = data.columns.get_level_values(0).rename(None)
        #convert to datetime data type
        data['Date'] = pd.to_datetime(data['Date'])
        if log:
            #log transform close price
            data['Log Close Price'] = np.log(data['Close'])
            #select columns
            data = data[['Date', 'Log Close Price']]
        else:
            data = data[['Date', 'Close']]
        return data
    except Exception as e:
        print(f"Error processing {stock_name} data: {e}")
        return None