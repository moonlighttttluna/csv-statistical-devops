import pandas as pd

def correlation_analysis(csv_file):
    df = pd.read_csv(csv_file)
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df.corr()