import pandas as pd
import pytest
from processors import (
    calculate_column_mean,
    calculate_column_median,
    calculate_column_std_dev,
    generate_statistical_summary,
    correlation_analysis
)

@pytest.fixture
def sample_data():
    """This creates fake data to test your functions."""
    data = {
        'Math': [80, 90, 100],
        'Science': [70, 80, 90]
    }
    return pd.DataFrame(data)

def test_mean(sample_data):
    result = calculate_column_mean(sample_data)
    assert result['Math'] == 90.0

def test_median(sample_data):
    result = calculate_column_median(sample_data)
    assert result['Math'] == 90.0

def test_std_dev(sample_data):
    result = calculate_column_std_dev(sample_data)
    # Std dev of [80, 90, 100] is 10.0
    assert result['Math'] == 10.0

def test_summary(sample_data):
    result = generate_statistical_summary(sample_data)
    # Check if the summary created the 'mean' row
    assert 'mean' in result.index

def test_correlation(sample_data):
    result = correlation_analysis(sample_data)
    # Correlation of a column with itself is always 1.0
    assert result.loc['Math', 'Math'] == 1.0
