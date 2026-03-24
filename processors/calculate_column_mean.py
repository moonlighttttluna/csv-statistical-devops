def calculate_column_mean(df):
    """
    Calculate mean of numeric columns from a DataFrame.
    Non-numeric columns are automatically ignored.
    """
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.mean()
