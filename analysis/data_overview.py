import pandas as pd

def data_overview(file_path):
    df = pd.read_csv(file_path)

    print("First 5 Rows")
    print(df.head())

    print("\nDataset Info")
    print(df.info())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nStatistical Summary")
    print(df.describe())

    return df