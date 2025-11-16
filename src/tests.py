# include your tests here 
# for example for your Progress report you should be able to load data from at least one API source.
from config import fred_api_key
from load import get_fred_data, get_stock_data

print('FRED Unemployment Rate Data Loading Test')
fred_unrate_data = get_fred_data('UNRATE', '2000-01-01', '2025-11-01', fred_api_key, freq = 'm')
print(fred_unrate_data.head())

print()

print('FRED GDP Data Loading Test')
fred_GDP_data = get_fred_data('GDP', '2010-01-01', '2023-11-01', fred_api_key, freq= 'q')
print(fred_GDP_data.head())

print()

print('FRED GDP Data Error Test')
try:
    fred_GDP_data = get_fred_data('GDasdasdP', '2010-01-01', '2023-11-01', fred_api_key, freq= 'q')
except:
    print('Error Expected')

print()

print('NVIDIA Data Loading Test')
nvidia_data = get_stock_data('NVDA', '2000-01-01', '2025-11-01', '1mo', True)
print(nvidia_data.head())

print()

print('TSLA Data Loading Test')
tesla_data = get_stock_data('TSLA', '2009-08-01', '2021-1-01', '1wk', True)
print(tesla_data.head())

print()

print('SPY Data Loading Test')
spy_data = get_stock_data('SPY', '1990-01-01', '2025-11-01', '1mo', True)
print(spy_data.head())

