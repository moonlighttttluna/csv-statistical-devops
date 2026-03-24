import pytest
import pandas as pd
from processors import calculate_column_mean, calculate_column_std_dev

@pytest.fixture
def sample_df():
    return pd.DataFrame({'A': [10, 20, 30], 'B': [5, 5, 5]})

def test_mean_logic(sample_df):
    result = calculate_column_mean(sample_df)
    assert result['A'] == 20.0
    assert result['B'] == 5.0

def test_std_logic(sample_df):
    result = calculate_column_std_dev(sample_df)
    assert result['B'] == 0.0  # Standard deviation of [5,5,5] is 0
