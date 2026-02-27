import pandas as pd

def generate_statistical_summary(csv_file):
    df = pd.read_csv(csv_file)
    return df.describe()