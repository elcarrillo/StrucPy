import pandas as pd
import pytest
import logging
from validate import validate_data

# Mock configuration for testing
MOCK_CONFIG = {
    "validation": {
        "check_missing_values": True,
        "check_duplicate_columns": True,
        "check_outliers": True,
        "missing_value_threshold": 0.1  # 10%
    }
}

@pytest.fixture
def mock_config(monkeypatch):
    """Fixture to mock the configuration loader."""
    from config_loader import load_config
    monkeypatch.setattr("validate.load_config", lambda: MOCK_CONFIG)

def test_validate_empty_dataframe(mock_config, caplog):
    """Test validation on an empty DataFrame."""
    df = pd.DataFrame()
    with caplog.at_level(logging.WARNING):
        results = validate_data(df)
    assert "The DataFrame is empty. Validation skipped." in caplog.text
    assert results["missing_values"] is False
    assert results["duplicate_columns"] is False
    assert not results["outliers"]

def test_validate_missing_values(mock_config, caplog):
    """Test validation for missing values."""
    df = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})  # 33.33% missing values
    with caplog.at_level(logging.WARNING):
        results = validate_data(df)
    assert "Missing values exceed threshold" in caplog.text
    assert results["missing_values"] is True

def test_validate_duplicate_columns(mock_config, caplog):
    """Test validation for duplicate columns."""
    df = pd.DataFrame({"A": [1, 2, 3], "A": [4, 5, 6]})  # Duplicate columns
    with caplog.at_level(logging.ERROR):  # Expect ERROR level logging
        results = validate_data(df)
    assert "Duplicate column names found" in caplog.text, "Expected duplicate column log not found."
    assert results["duplicate_columns"] is True, "Duplicate column result not updated."


def test_validate_outliers(mock_config, caplog):
    """Test validation for outliers."""
    df = pd.DataFrame({"A": [1, 2, 100], "B": [4, 5, 6]})  # Outlier in column A
    with caplog.at_level(logging.WARNING):  # Expect WARNING level logging
        results = validate_data(df)
    assert "Outliers detected in column 'A'" in caplog.text, "Expected outlier log not found."
    assert "A" in results["outliers"], "Outlier column not added to results."


def test_validate_no_issues(mock_config, caplog):
    """Test validation on a clean DataFrame."""
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    with caplog.at_level(logging.INFO):
        results = validate_data(df)
    assert "Data validation complete." in caplog.text
    assert results["missing_values"] is False
    assert results["duplicate_columns"] is False
    assert not results["outliers"]
