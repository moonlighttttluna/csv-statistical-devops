import pandas as pd

def generate_statistical_summary(csv_file):
    df = pd.read_csv(csv_file)
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.describe()