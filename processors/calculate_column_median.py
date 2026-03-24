def calculate_column_median(df):
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.median()
