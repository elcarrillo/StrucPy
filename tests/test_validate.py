import pandas as pd
from src.validate import validate_data

def test_validate_data_missing_values(capsys):
    df = pd.DataFrame({"A": [1, 2, None], "B": [4, None, 6]})
    validate_data(df)

    # Capture printed output and check for warnings
    captured = capsys.readouterr()
    assert "Missing values detected" in captured.out

def test_validate_data_no_missing_values(capsys):
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    validate_data(df)

    # Capture printed output and check for validation message
    captured = capsys.readouterr()
    assert "Data validation complete." in captured.out

def test_validate_data_duplicate_columns(capsys):
    df = pd.DataFrame({"A": [1, 2, 3], "A": [4, 5, 6]})  # Duplicate column names
    validate_data(df)

    # Capture printed output and check for error message
    captured = capsys.readouterr()
    assert "Duplicate column names found" in captured.out

def test_validate_data_outliers(capsys):
    df = pd.DataFrame({"A": [1, 2, 100], "B": [4, 5, 6]})
    validate_data(df)

    # Capture printed output and check for outlier warnings
    captured = capsys.readouterr()
    assert "Outliers detected in column A" in captured.out
