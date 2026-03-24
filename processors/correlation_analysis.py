def correlation_analysis(df):
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.corr()
