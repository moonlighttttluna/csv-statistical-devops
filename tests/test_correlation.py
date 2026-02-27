import pandas as pd
from processors.correlation_analysis import correlation_analysis

def test_correlation_analysis():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [1, 2, 3]
    })

    test_file = "test_corr.csv"
    df.to_csv(test_file, index=False)

    result = correlation_analysis(test_file)

    assert result.loc["A", "B"] == 1.0