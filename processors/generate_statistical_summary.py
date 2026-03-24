def generate_statistical_summary(df):
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.describe()
