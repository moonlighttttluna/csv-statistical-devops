import pandas as pd
from processors.generate_statistical_summary import generate_statistical_summary

def test_generate_statistical_summary():
    df = pd.DataFrame({
        "Math": [10, 20, 30],
    })

    test_file = "test_summary.csv"
    df.to_csv(test_file, index=False)

    result = generate_statistical_summary(test_file)

    assert "mean" in result.index