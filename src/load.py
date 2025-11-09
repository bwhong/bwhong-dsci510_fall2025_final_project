import os
# os.environ["KAGGLE_CONFIG_DIR"] = "/home/alexey/"
import pandas as pd
import requests
import yfinance as yf
from fredapi import Fred

# --- 1. DOWNLOAD DATA FROM FRED ---

def get_fred_data(dataset, observation_start, observation_end, frequency = 'm', api_key):
    """
    Downloads a specific file from FRED, extracts it,
    and loads it into a pandas DataFrame.

    :param dataset: Dataset to extract
    :param observation_start: Observation Start Date
    :param observation_end: Observation End Date
    :param api_key_file: API Key File
    :param extract_dir: Directory to extract files into
    :return: pandas DataFrame or None
    """
    print(f"--- Loading data from FRED: {dataset} ---")
    try:
        print(f"Downloading {dataset}...")
        fred = Fred(api_key = api_key)
        data = fred.get_series(dataset,  observation_start, observation_end, frequency)
        data = data.reset_index()
        data.columns = ['Date', 'Value']
        return data
    except Exception as e:
        print(f"Error loading data from FRED: {e}")
        return None


# --- 2. DOWNLOAD FILE FROM WEB ---

def get_web_csv_data(url):
    """
    Downloads a CSV file directly from a URL into a pandas DataFrame.

    :param url: The direct URL to the .csv file
    :return: pandas DataFrame or None
    """
    print(f"--- Loading data from Web URL: {url[:50]}... ---")
    try:
        # pandas can read a CSV directly from a URL
        df = pd.read_csv(url)
        print("Web CSV data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data from URL: {e}")
        return None


# --- 3. SCRAPE DATA FROM WEBPAGE (WIKIPEDIA) ---
def get_wikipedia_table_data(url, table_index=0):
    """
    Scrapes a specific table from a Wikipedia page into a pandas DataFrame.

    MODIFIED: Added a User-Agent header to prevent 403 Forbidden errors.

    :param url: The URL of the Wikipedia page
    :param table_index: The 0-based index of the table to scrape
    :return: pandas DataFrame or None
    """
    print(f"--- Scraping table from Wikipedia: {url[:50]}... ---")

    # --- MODIFICATION ---
    # Set a User-Agent to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # --- END MODIFICATION ---

    try:
        # --- MODIFICATION ---
        # Use requests to get the page with the headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}. Unable to fetch page.")
            return None
        # --- END MODIFICATION ---

        # Pass the HTML content (response.text) to pandas
        # It returns a LIST of DataFrames (all tables on the page)
        tables = pd.read_html(response.text, flavor='bs4')

        if tables:
            print(f"Found {len(tables)} tables. Extracting table at index {table_index}...")
            # We select the specific table we want
            df = tables[table_index]
            print("Wikipedia table scraped successfully.")
            return df
        else:
            print("No tables found on the page.")
            return None

    except Exception as e:
        print(f"Error scraping Wikipedia table: {e}")
        return None

