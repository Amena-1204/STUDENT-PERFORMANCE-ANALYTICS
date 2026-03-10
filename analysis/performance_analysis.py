import matplotlib.pyplot as plt
import seaborn as sns

def performance_analysis(df):

    print("\nAverage Scores")

    print(df[['Math','Science','English']].mean())

    sns.histplot(df['Math'], kde=True)
    plt.title("Math Score Distribution")
    plt.show()