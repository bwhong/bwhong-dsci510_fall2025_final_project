import os
from config import fred_api_key, UNRATE_DATASET, SPY_DATASET, NVIDIA_DATASET, START_DATE, END_DATE, AI_BOOM_START_DATE, UNRATE_DATASET_COLOR, SPY_DATASET_COLOR, NVIDIA_DATASET_COLOR, RESULTS_DIR
from load import get_fred_data, get_stock_data
from analyze import plot_statistics, plot_correlation_analysis
from process import process_fred_data, process_stock_data

if __name__ == "__main__":
    # --- FRED Data ---
    fred_raw_data = get_fred_data(UNRATE_DATASET, START_DATE, END_DATE, fred_api_key)
    fred_processed_data = process_fred_data(fred_raw_data, 'Unemployment Rate')
    print("\n" + "=" * 50 + "\n")

    # --- NVIDIA Data ---
    nvidia_raw_data = get_stock_data(NVIDIA_DATASET,  START_DATE, END_DATE, '1mo', True)
    nvidia_processed_data  = process_stock_data(nvidia_raw_data, 'SPY')
    print("\n" + "=" * 50 + "\n")

    # --- SPY Data ---
    spy_raw_data = get_stock_data(SPY_DATASET,  START_DATE, END_DATE, '1mo', True)
    spy_processed_data  = process_stock_data(spy_raw_data, 'SPY')
    print("\n" + "=" * 50 + "\n")

    # plot individual results
    plot_statistics(fred_processed_data, 'Unemployment Rate', result_dir=RESULTS_DIR, color = UNRATE_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(nvidia_processed_data, 'NVIDIA', result_dir=RESULTS_DIR, color = NVIDIA_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(spy_processed_data, 'SPY', result_dir=RESULTS_DIR, color = SPY_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    print("\n--- Data collection and plotting complete. Check the 'results' directory. ---")