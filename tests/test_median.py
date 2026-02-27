import pandas as pd
from processors.calculate_column_median import calculate_column_median

def test_calculate_column_median():
    df = pd.DataFrame({
        "Math": [80, 90, 100],
        "Science": [70, 80, 90]
    })

    test_file = "test_median.csv"
    df.to_csv(test_file, index=False)

    result = calculate_column_median(test_file)

    assert result["Math"] == 90
    assert result["Science"] == 80