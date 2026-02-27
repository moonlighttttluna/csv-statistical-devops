import pandas as pd
from processors.calculate_column_mean import calculate_column_mean

def test_calculate_column_mean():
    df = pd.DataFrame({
        "Math": [80, 90, 100],
        "Science": [70, 80, 90]
    })

    test_file = "test_mean.csv"
    df.to_csv(test_file, index=False)

    result = calculate_column_mean(test_file)

    assert result["Math"] == 90
    assert result["Science"] == 80