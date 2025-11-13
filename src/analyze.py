import os
import matplotlib.pyplot as plt


# --- PLOT STATISTICS ---
def plot_statistics(df, dataset_name, color, result_dir="plots", notebook_plot=False):
    """
    Generates and saves basic plots for a given DataFrame.

    :param result_dir: where to place plots
    :param df: The pandas DataFrame
    :param dataset_name: A name for titling plots (e.g., 'Titanic')
    """
    print(f"--- Plotting statistics for {dataset_name} ---")

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
