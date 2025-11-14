import os
import matplotlib.pyplot as plt
import numpy as np


# --- PLOT STATISTICS ---
def plot_statistics(df, dataset_name, color, result_dir="plots", notebook_plot=False):
    """
    Generates and saves basic plots for a given DataFrame.

    :param df: The pandas DataFrame
    :param dataset_name: A name for titling plots (e.g., 'Titanic')
    :param color: The color for the plots
    :param result_dir: where to place plots
    :param notebook_plot: whether to send plot to results directory or just display it in notebook
    """
    print(f"--- Plotting basic statistics for {dataset_name} ---")

    # Ensure a directory for plots exists
    os.makedirs(result_dir, exist_ok=True)

    # Identify numerical and categorical columns for plotting
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    datetime_cols = df.select_dtypes(include=['datetime']).columns

    print(datetime_cols)
    # Plot 1: Histogram (for a numerical column)
    if not numerical_cols.empty:
        col_to_plot = numerical_cols[0]
        plt.figure(figsize=(10, 6))
        df[col_to_plot].hist(bins=30, color = color, edgecolor='black')
        plt.title(f'Histogram of {col_to_plot} - {dataset_name}')
        plt.xlabel(col_to_plot)
        plt.ylabel('Frequency')
        plt.grid(axis='y')
        if not notebook_plot:
            plt.savefig(f'{result_dir}/{dataset_name}_histogram.png')
            print(f"Saved histogram for {col_to_plot}")
            plt.close()
        else:
            plt.plot()

    # Plot 2: Line Plot
    if not datetime_cols.empty:
        col1 = datetime_cols[0]
        col2 = numerical_cols[0]
        plt.figure(figsize=(10, 6))
        plt.plot(df[col1], df[col2], color = color, alpha=0.5)
        plt.title(f'{col2} Over Time')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.grid(True)
        if not notebook_plot:
            plt.savefig(f'{result_dir}/{dataset_name}_lineplot.png')
            print(f"Saved line plot for {col1} vs {col2}")
            plt.close()
        else:
            plt.plot()

def plot_correlation_analysis(df1, df2, color1, color2, dataset_name1, dataset_name2, df3 = None, color3 = None, dataset_name3 = None, result_dir="plots", notebook_plot=False):
    """
    Generates and saves correlation plots for given DataFrames.

    :param df1: the first pandas dataframe
    :param df2: the second pandas dataframe
    :param color1: the color for the first pandas dataframe
    :param color2: the color for the second pandas dataframe
    :param dataset_name1: A name for titling plots for the first pandas dataframe
    :param dataset_name2: A name for titling plots for the second pandas dataframe
    :param df3: optional third pandas dataframe
    :param color3: optional color for the third pandas dataframe
    :param dataset_name2: An optional name for titling plots for the third pandas dataframe
    :param result_dir: where to place plots
    :param notebook_plot: whether to send plot to results directory or just display it in notebook
    """
    if df3 is None:
        print(f"--- Plotting statistics for {dataset_name1} and {dataset_name2}---")
        #dual axis line chart
        fig, ax1 = plt.subplots()
        plt.title(f'{dataset_name1} and {dataset_name2} over Time')
        plt.plot(df1['Date'], df1.iloc[:, 1], color = color1)
        ax1.set_xlabel('Date')
        ax1.set_ylabel(dataset_name1, color='Black')
        ax2 = ax1.twinx()
        plt.plot(df2['Date'], df2.iloc[:, 1], color= color2)
        ax2.set_ylabel(dataset_name2, color='Black')

        #scatter
        fig, ax1 = plt.subplots()
        plt.title(f'Scatter Plot of {dataset_name1} and {dataset_name2}')
        plt.scatter(df1.iloc[:, 1], df2.iloc[:, 1], color = color1)
        ax1.set_xlabel(dataset_name1, color='Black')
        ax1.set_ylabel(dataset_name2, color='Black')
        slope, intercept = np.polyfit(df1.iloc[:, 1], df2.iloc[:, 1], 1)  # linear regression
        reg_line = (slope * df1.iloc[:, 1]) + intercept
        plt.plot(df1.iloc[:, 1], reg_line, color='red', linewidth=2, label=f'Regression line: y={slope:.2f}x+{intercept:.2f}')

        #heatmap
    else:
        print(f"--- Plotting statistics for {dataset_name1}, {dataset_name2}, and {dataset_name3}---")
    