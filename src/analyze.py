import os
import matplotlib.pyplot as plt
import seaborn as sns
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

def plot_correlation_analysis(df1, df2, color1, color2, dataset_name1, dataset_name2, df3 = None, color3 = None, dataset_name3 = None, result_dir="plots", ai_boom = None, notebook_plot=False):
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
        ax1.set_title(f'{dataset_name1} and {dataset_name2} over Time')
        ax1.plot(df1['Date'], df1.iloc[:, 1], color = color1)
        ax1.set_xlabel('Date')
        ax1.set_ylabel(dataset_name1, color='Black')
        ax2 = ax1.twinx()
        ax2.plot(df2['Date'], df2.iloc[:, 1], color= color2)
        ax2.set_ylabel(dataset_name2, color='Black')
        if not notebook_plot:
            if ai_boom == 'Post':
                plt.savefig(f'{result_dir}/Post_AI_Boom_{dataset_name1}_{dataset_name2}_dual_axis_line_chart.png')
            elif ai_boom == 'Pre':
                plt.savefig(f'{result_dir}/Pre_AI_Boom_{dataset_name1}_{dataset_name2}_dual_axis_line_chart.png')
            else:
                plt.savefig(f'{result_dir}/{dataset_name1}_{dataset_name2}_dual_axis_line_chart.png')
            print(f"Saved Dual Axis Line Chart for {dataset_name1} and {dataset_name2}")
            plt.close()
        else:
            plt.plot()

        #scatter
        fig, ax1 = plt.subplots()
        ax1.set_title(f'Scatter Plot of {dataset_name1} and {dataset_name2}')
        temp_df = df1.merge(df2, on = 'Date')
        temp_df.columns = ['Date', dataset_name1, dataset_name2]
        sns.regplot(x=temp_df.columns[1], y=temp_df.columns[2], data=temp_df, scatter_kws={'color':color1}, ci=95, color = 'red')
        ax1.set_xlabel(dataset_name1, color='Black')
        ax1.set_ylabel(dataset_name2, color='Black')
        if not notebook_plot:
            if ai_boom == 'Post':
                plt.savefig(f'{result_dir}/Post_AI_Boom_{dataset_name1}_{dataset_name2}_scatter_plot.png')
            elif ai_boom == 'Pre':
                plt.savefig(f'{result_dir}/Pre_AI_Boom_{dataset_name1}_{dataset_name2}_scatter_plot.png')
            else:
                plt.savefig(f'{result_dir}/{dataset_name1}_{dataset_name2}_scatter_plot.png')
            print(f"Saved Scatter Plot for {dataset_name1} and {dataset_name2}")
            plt.close()
        else:
            plt.plot()


        #heatmap
        fig, ax1 = plt.subplots()
        ax1.set_title(f'Heatmap of {dataset_name1} and {dataset_name2}')
        if df1.columns[1] == df2.columns[1]:
            df1.columns = ['Date', dataset_name1]
            df2.columns = ['Date', dataset_name2]
        temp_df_corr = df1.merge(df2, on = 'Date').drop(columns = {'Date'}).corr()
        plt.xticks(rotation=0) 
        plt.yticks(rotation=0)
        sns.heatmap(temp_df_corr, annot=True)
        if not notebook_plot:
            if ai_boom == 'Post':
                plt.savefig(f'{result_dir}/Post_AI_Boom_{dataset_name1}_{dataset_name2}_heatmap.png')
            elif ai_boom == 'Pre':
                plt.savefig(f'{result_dir}/Pre_AI_Boom_{dataset_name1}_{dataset_name2}_heatmap.png')
            else:
                plt.savefig(f'{result_dir}/{dataset_name1}_{dataset_name2}_heatmap.png')
            print(f"Saved Heatmap for {dataset_name1} and {dataset_name2}")
            plt.close()
        else:
            plt.plot()
    else:
        print(f"--- Plotting statistics for {dataset_name1} and {dataset_name2} and {dataset_name3}---")
        #dual axis line chart
        fig, ax1 = plt.subplots()
        ax1.set_title(f'{dataset_name1}, {dataset_name2}, and {dataset_name3} over Time')
        sns.lineplot(data=df1, x="Date", y=df1.columns[1], ax=ax1, label=dataset_name1, color=color1, legend = False)
        sns.lineplot(data=df2, x="Date", y=df2.columns[1], ax=ax1, label=dataset_name2, color=color2, legend = False)
        ax1.set_xlabel('Date')
        ax1.set_ylabel(dataset_name1, color='Black')
        ax2 = ax1.twinx()
        sns.lineplot(data=df3, x="Date", y=df3.columns[1], ax=ax2, label=dataset_name3, color=color3, legend = False)
        ax2.set_ylabel(dataset_name3, color='Black')
        handles1, labels1 = ax1.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(handles1 + handles2,
           labels1 + labels2,
           loc='upper left',
           frameon=True, prop={'size': 7})
        if not notebook_plot:
            if ai_boom == 'Post':
                plt.savefig(f'{result_dir}/Post_AI_Boom_{dataset_name1}_{dataset_name2}_{dataset_name3}_dual_axis_line_chart.png', bbox_inches='tight')
            elif ai_boom == 'Pre':
                plt.savefig(f'{result_dir}/Pre_AI_Boom_{dataset_name1}_{dataset_name2}_{dataset_name3}_dual_axis_line_chart.png', bbox_inches='tight')
            else:
                plt.savefig(f'{result_dir}/{dataset_name1}_{dataset_name2}_{dataset_name3}_dual_axis_line_chart.png', bbox_inches='tight')
            print(f"Saved Dual Axis Line Chart for {dataset_name1}, {dataset_name2}, and {dataset_name3}")
            plt.close()
        else:
            plt.plot()
        #heatmap
        fig, ax1 = plt.subplots()
        ax1.set_title(f'Heatmap of {dataset_name1}, {dataset_name2}, and {dataset_name3}')
        if df1.columns[1] == df2.columns[1]:
            df1.columns = ['Date', dataset_name1]
            df2.columns = ['Date', dataset_name2]
        temp_df_corr = df1.merge(df2, on = 'Date').merge(df3, on = 'Date').drop(columns = {'Date'}).corr()
        sns.heatmap(temp_df_corr, annot=True)
        plt.xticks(rotation=0, fontsize=8) 
        plt.yticks(rotation=90, fontsize=8) 
        if not notebook_plot:
            if ai_boom == 'Post':
                plt.savefig(f'{result_dir}/Post_AI_Boom_{dataset_name1}_{dataset_name2}_{dataset_name3}_heatmap.png', bbox_inches='tight')
            elif ai_boom == 'Pre':
                plt.savefig(f'{result_dir}/Pre_AI_Boom_{dataset_name1}_{dataset_name2}_{dataset_name3}_heatmap.png', bbox_inches='tight')
            else:
                plt.savefig(f'{result_dir}/{dataset_name1}_{dataset_name2}_{dataset_name3}_heatmap.png', bbox_inches='tight')
            print(f"Saved Heatmap for {dataset_name1}, {dataset_name2}, and {dataset_name3}")
            plt.close()
        else:
            plt.plot()