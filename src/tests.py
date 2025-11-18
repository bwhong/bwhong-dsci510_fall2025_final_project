from config import fred_api_key
from load import get_fred_data, get_stock_data
from analyze import plot_statistics, plot_correlation_analysis
from process import process_fred_data, process_stock_data

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

print()

print('Fred Processing Data Test')
fred_unrate_processed_data = process_fred_data(fred_unrate_data, 'Unemployment Rate', True)
print(fred_unrate_data.head())

print()

print('SPY Processing Test')
spy_processed_data = process_stock_data(spy_data, 'SPY')
print(spy_processed_data)

print()

print('Plot Statistic test')
plot_statistics(spy_processed_data, 'SPY',  color = 'blue')

print()

print('Plot Correlation Analysis')
plot_correlation_analysis(spy_processed_data, fred_unrate_processed_data, 'blue', 'gray', 'SPY Log Close Price', 'Unemployment Rate')
