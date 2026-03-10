import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def demographic_analysis(
    df: pd.DataFrame, 
    demographic_col: str = 'gender', 
    score_col: str = 'math_score'
):
    """
    Performs demographic analysis by visualizing student distribution and performance.

    Generates two side-by-side plots:
    1. A count plot for the distribution of a demographic category.
    2. A box plot showing the score distribution within that demographic category.

    Args:
        df (pd.DataFrame): The DataFrame containing student performance data.
        demographic_col (str): The column name for the demographic variable (e.g., 'gender').
        score_col (str): The column name for the score to be analyzed (e.g., 'math_score').
    """
    if demographic_col not in df.columns or score_col not in df.columns:
        print(f"Error: One or both columns ('{demographic_col}', '{score_col}') not found in the DataFrame.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(f'Analysis of {score_col.replace("_", " ").title()} by {demographic_col.replace("_", " ").title()}', fontsize=16)

    # Plot 1: Distribution of the demographic variable
    sns.countplot(ax=axes[0], x=demographic_col, data=df)
    axes[0].set_title(f'{demographic_col.replace("_", " ").title()} Distribution')

    # Plot 2: Score distribution by the demographic variable
    sns.boxplot(ax=axes[1], x=demographic_col, y=score_col, data=df)
    axes[1].set_title(f'{score_col.replace("_", " ").title()} by {demographic_col.replace("_", " ").title()}')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()