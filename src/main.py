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

    # Plot Individual Statistical Plots
    plot_statistics(fred_processed_data, 'Unemployment Rate', result_dir=RESULTS_DIR, color = UNRATE_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(nvidia_processed_data, 'NVIDIA', result_dir=RESULTS_DIR, color = NVIDIA_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(spy_processed_data, 'SPY', result_dir=RESULTS_DIR, color = SPY_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    #Plot Correlation Analysis Plots
    plot_correlation_analysis(nvidia_processed_data, fred_processed_data, NVIDIA_DATASET_COLOR, UNRATE_DATASET_COLOR, 'NVIDIA Log Close Price ($)', 'Unemployment Rate (%)', result_dir=RESULTS_DIR)
    print("\n" + "=" * 50 + "\n")
    
    plot_correlation_analysis(nvidia_processed_data, spy_processed_data, NVIDIA_DATASET_COLOR, SPY_DATASET_COLOR, 'NVIDIA Log Close Price ($)', 'SPY Log Close Price($)', fred_processed_data, UNRATE_DATASET_COLOR, 'Unemployment Rate (%)', result_dir=RESULTS_DIR)
    print("\n" + "=" * 50 + "\n")

    #plot Pre AI Boom Correlation Analysis Plots
    fred_processed_data_pre_ai_boom = fred_processed_data[fred_processed_data['Date'] < AI_BOOM_START_DATE]
    nvidia_processed_data_pre_ai_boom = nvidia_processed_data[nvidia_processed_data['Date'] < AI_BOOM_START_DATE]
    spy_processed_data_pre_ai_boom = spy_processed_data[spy_processed_data['Date'] < AI_BOOM_START_DATE]
    plot_correlation_analysis(nvidia_processed_data_pre_ai_boom, spy_processed_data_pre_ai_boom, NVIDIA_DATASET_COLOR, SPY_DATASET_COLOR, 'NVIDIA Log Close Price ($)', 'SPY Log Close Price($)', fred_processed_data_pre_ai_boom, UNRATE_DATASET_COLOR, 'Unemployment Rate (%)', result_dir= RESULTS_DIR, ai_boom= 'Pre')
    
    print("\n" + "=" * 50 + "\n")

    #plot Post AI Boom Correlation Analysis Plots
    fred_processed_data_post_ai_boom = fred_processed_data[fred_processed_data['Date'] >= AI_BOOM_START_DATE]
    nvidia_processed_data_post_ai_boom = nvidia_processed_data[nvidia_processed_data['Date'] >= AI_BOOM_START_DATE]
    spy_processed_data_post_ai_boom = spy_processed_data[spy_processed_data['Date'] >= AI_BOOM_START_DATE]
    plot_correlation_analysis(nvidia_processed_data_post_ai_boom, spy_processed_data_post_ai_boom, NVIDIA_DATASET_COLOR, SPY_DATASET_COLOR, 'NVIDIA Log Close Price ($)', 'SPY Log Close Price($)', fred_processed_data_post_ai_boom, UNRATE_DATASET_COLOR, 'Unemployment Rate (%)', result_dir= RESULTS_DIR, ai_boom= 'Post')
    
    print("\n" + "=" * 50 + "\n")

    print("\n--- Data collection and plotting complete. Check the 'results' directory. ---")