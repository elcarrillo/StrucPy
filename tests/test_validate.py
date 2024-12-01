import pandas as pd
import pytest
from validate import validate_data

def test_validate_data_missing_values(capsys):
    """Test handling of missing values."""
    df = pd.DataFrame({"A": [1, 2, None], "B": [4, None, 6]})
    validate_data(df)

    # Capture printed output and check for warnings
    captured = capsys.readouterr()
    assert "Warning: Missing values detected" in captured.out or "Warning: Missing values exceed threshold" in captured.out

def test_validate_data_no_missing_values(capsys):
    """Test validation when no missing values exist."""
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    validate_data(df)

    # Capture printed output
    captured = capsys.readouterr()
    assert "Data validation complete." in captured.out

def test_validate_data_below_threshold_missing_values(capsys):
    """Test handling of missing values below the threshold."""
    df = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, 6]})  # 1 missing value (16.67% if 6 total cells)
    validate_data(df)

    # Capture printed output and check for informational warning
    captured = capsys.readouterr()
    assert "Info: Missing values detected" in captured.out

def test_validate_data_duplicate_columns(capsys):
    """Test handling of duplicate column names."""
    df = pd.DataFrame({"A": [1, 2, 3], "A": [4, 5, 6]})  # Duplicate column names
    validate_data(df)

    # Capture printed output and check for error message
    captured = capsys.readouterr()
    assert "Error: Duplicate column names found" in captured.out

def test_validate_data_outliers(capsys):
    """Test handling of outliers in numeric columns."""
    df = pd.DataFrame({"A": [1, 2, 100], "B": [4, 5, 6]})  # Outlier in column A
    validate_data(df)

    # Capture printed output and check for outlier warnings
    captured = capsys.readouterr()
    assert "Warning: Outliers detected in column 'A'" in captured.out

def test_validate_data_no_outliers(capsys):
    """Test validation when no outliers are present."""
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    validate_data(df)

    # Capture printed output
    captured = capsys.readouterr()
    assert "Data validation complete." in captured.out
