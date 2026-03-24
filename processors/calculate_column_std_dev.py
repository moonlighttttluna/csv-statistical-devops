def calculate_column_std_dev(df):
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.std()
