import matplotlib.pyplot as plt

def subject_analysis(df):

    averages = df[['Math','Science','English','Computer']].mean()

    averages.plot(kind='bar')

    plt.title("Average Subject Scores")

    plt.show()