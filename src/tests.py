# include your tests here 
# for example for your Progress report you should be able to load data from at least one API source.
from config import fred_api_key
from load import get_fred_data

print('FRED Unemployment Rate Data Loading Example')
fred_unrate_data = get_fred_data('UNRATE', '2000-01-01', '2025-11-01', fred_api_key, freq = 'm')
print(fred_unrate_data.head())

print()

print('FRED GDP Data Loading Example')
fred_GDP_data = get_fred_data('GDP', '2010-01-01', '2023-11-01', fred_api_key, freq= 'q')
print(fred_GDP_data.head())

