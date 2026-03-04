import pandas as pd

def calculate_column_median(csv_file):
    df = pd.read_csv(csv_file)
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.median()