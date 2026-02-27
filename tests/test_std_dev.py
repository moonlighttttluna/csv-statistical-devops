import pandas as pd
from processors.calculate_column_std_dev import calculate_column_std_dev

def test_calculate_column_std_dev():
    df = pd.DataFrame({
        "Math": [10, 20, 30],
    })

    test_file = "test_std.csv"
    df.to_csv(test_file, index=False)

    result = calculate_column_std_dev(test_file)

    assert round(result["Math"], 2) == 10.0