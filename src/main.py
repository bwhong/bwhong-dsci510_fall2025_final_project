from config import fred_api_key, UNRATE_DATASET, SPY_DATASET, NVIDIA_DATASET, START_DATE, END_DATE, AI_BOOM_START_DATE, UNRATE_DATASET_COLOR, SPY_DATASET_COLOR, NVIDIA_DATASET_COLOR, RESULTS_DIR, UNRATE_DATASET_PRIMARY_COLUMN_NAME, COVID_RAW, COVID_SMOOTHED, UNRATE_PLOT_BASE_TITLE, UNRATE_COVID_PLOT_BASE_TITLE, COVID_SMOOTHED, STOCK_SAMPLING_FREQUENCY, USE_RAW_STOCK_DATA, USE_LOG_CLOSE_STOCK_PRICE, SPY_DATASET_STOCK_NAME, SPY_PLOT_BASE_TITLE, SPY_LOG_PLOT_BASE_TITLE, NVIDIA_DATASET_STOCK_NAME, NVIDIA_PLOT_BASE_TITLE, NVIDIA_LOG_PLOT_BASE_TITLE, PRE_AI_BOOM, POST_AI_BOOM, UNRATE_SAMPLING_FREQUENCY
from load import get_fred_data, get_stock_data
from analyze import plot_statistics, plot_correlation_analysis
from process import process_fred_data, process_stock_data

if __name__ == "__main__":
    # --- FRED Data ---
    fred_raw_data = get_fred_data(UNRATE_DATASET, START_DATE, END_DATE, fred_api_key, UNRATE_SAMPLING_FREQUENCY)
    fred_processed_data_covid = process_fred_data(fred_raw_data, UNRATE_DATASET_PRIMARY_COLUMN_NAME, COVID_RAW)
    fred_processed_data = process_fred_data(fred_raw_data, UNRATE_DATASET_PRIMARY_COLUMN_NAME, COVID_SMOOTHED)
    print("\n" + "=" * 50 + "\n")

    # --- NVIDIA Data ---
    nvidia_raw_data = get_stock_data(NVIDIA_DATASET,  START_DATE, END_DATE, STOCK_SAMPLING_FREQUENCY)
    nvidia_processed_data  = process_stock_data(nvidia_raw_data, NVIDIA_DATASET_STOCK_NAME, log = USE_RAW_STOCK_DATA)
    nvidia_processed_log_data  = process_stock_data(nvidia_raw_data, NVIDIA_DATASET_STOCK_NAME, log = USE_LOG_CLOSE_STOCK_PRICE)
    print("\n" + "=" * 50 + "\n")

    # --- SPY Data ---
    spy_raw_data = get_stock_data(SPY_DATASET,  START_DATE, END_DATE, STOCK_SAMPLING_FREQUENCY)
    spy_processed_data  = process_stock_data(spy_raw_data, SPY_DATASET_STOCK_NAME, log = USE_RAW_STOCK_DATA)
    spy_processed_log_data  = process_stock_data(spy_raw_data, SPY_DATASET_STOCK_NAME, log = USE_LOG_CLOSE_STOCK_PRICE)
    print("\n" + "=" * 50 + "\n")

    # Plot Individual Statistical Plots
    plot_statistics(fred_processed_data_covid, UNRATE_COVID_PLOT_BASE_TITLE, result_dir=RESULTS_DIR, color = UNRATE_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(fred_processed_data, UNRATE_PLOT_BASE_TITLE, result_dir=RESULTS_DIR, color = UNRATE_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(nvidia_processed_data, NVIDIA_PLOT_BASE_TITLE, result_dir=RESULTS_DIR, color = NVIDIA_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(nvidia_processed_log_data, NVIDIA_LOG_PLOT_BASE_TITLE, result_dir=RESULTS_DIR, color = NVIDIA_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(spy_processed_data, SPY_PLOT_BASE_TITLE, result_dir=RESULTS_DIR, color = SPY_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    plot_statistics(spy_processed_log_data, SPY_LOG_PLOT_BASE_TITLE, result_dir=RESULTS_DIR, color = SPY_DATASET_COLOR)
    print("\n" + "=" * 50 + "\n")

    #Plot Correlation Analysis Plots
    plot_correlation_analysis(nvidia_processed_log_data, fred_processed_data, NVIDIA_DATASET_COLOR, UNRATE_DATASET_COLOR, NVIDIA_LOG_PLOT_BASE_TITLE, UNRATE_PLOT_BASE_TITLE, result_dir=RESULTS_DIR)
    print("\n" + "=" * 50 + "\n")
    
    plot_correlation_analysis(spy_processed_log_data, fred_processed_data, SPY_DATASET_COLOR, UNRATE_DATASET_COLOR, SPY_LOG_PLOT_BASE_TITLE, UNRATE_PLOT_BASE_TITLE, result_dir=RESULTS_DIR)
    print("\n" + "=" * 50 + "\n")

    plot_correlation_analysis(nvidia_processed_log_data, spy_processed_log_data, NVIDIA_DATASET_COLOR, SPY_DATASET_COLOR, NVIDIA_LOG_PLOT_BASE_TITLE, SPY_LOG_PLOT_BASE_TITLE, fred_processed_data, UNRATE_DATASET_COLOR, UNRATE_PLOT_BASE_TITLE, result_dir=RESULTS_DIR)
    print("\n" + "=" * 50 + "\n")

    #plot Pre AI Boom Correlation Analysis Plots
    fred_processed_data_pre_ai_boom = fred_processed_data[fred_processed_data['Date'] < AI_BOOM_START_DATE]
    nvidia_processed_log_data_pre_ai_boom = nvidia_processed_log_data[nvidia_processed_log_data['Date'] < AI_BOOM_START_DATE]
    spy_processed_log_data_pre_ai_boom = spy_processed_log_data[spy_processed_log_data['Date'] < AI_BOOM_START_DATE]
    plot_correlation_analysis(nvidia_processed_log_data_pre_ai_boom, fred_processed_data_pre_ai_boom, NVIDIA_DATASET_COLOR, UNRATE_DATASET_COLOR, NVIDIA_LOG_PLOT_BASE_TITLE, UNRATE_PLOT_BASE_TITLE, result_dir= RESULTS_DIR, ai_boom= PRE_AI_BOOM)
    plot_correlation_analysis(nvidia_processed_log_data_pre_ai_boom, spy_processed_log_data_pre_ai_boom, NVIDIA_DATASET_COLOR, SPY_DATASET_COLOR, NVIDIA_LOG_PLOT_BASE_TITLE, SPY_LOG_PLOT_BASE_TITLE, fred_processed_data_pre_ai_boom, UNRATE_DATASET_COLOR, UNRATE_PLOT_BASE_TITLE, result_dir= RESULTS_DIR, ai_boom= PRE_AI_BOOM)
    
    print("\n" + "=" * 50 + "\n")

    #plot Post AI Boom Correlation Analysis Plots
    fred_processed_data_post_ai_boom = fred_processed_data[fred_processed_data['Date'] >= AI_BOOM_START_DATE]
    nvidia_processed_log_data_post_ai_boom = nvidia_processed_log_data[nvidia_processed_log_data['Date'] >= AI_BOOM_START_DATE]
    spy_processed_log_data_post_ai_boom = spy_processed_log_data[spy_processed_log_data['Date'] >= AI_BOOM_START_DATE]
    plot_correlation_analysis(nvidia_processed_log_data_post_ai_boom, fred_processed_data_post_ai_boom, NVIDIA_DATASET_COLOR, UNRATE_DATASET_COLOR, NVIDIA_LOG_PLOT_BASE_TITLE, UNRATE_PLOT_BASE_TITLE, result_dir= RESULTS_DIR, ai_boom= POST_AI_BOOM)
    plot_correlation_analysis(nvidia_processed_log_data_post_ai_boom, spy_processed_log_data_post_ai_boom, NVIDIA_DATASET_COLOR, SPY_DATASET_COLOR, NVIDIA_LOG_PLOT_BASE_TITLE, SPY_LOG_PLOT_BASE_TITLE, fred_processed_data_post_ai_boom, UNRATE_DATASET_COLOR, UNRATE_PLOT_BASE_TITLE, result_dir= RESULTS_DIR, ai_boom= POST_AI_BOOM)

    print("\n" + "=" * 50 + "\n")

    print("\n--- Data collection and plotting complete. Check the 'results' directory. ---")