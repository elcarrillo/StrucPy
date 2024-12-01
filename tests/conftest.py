import pytest
import pandas as pd
import sys
import os

# Add src/ to the module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


@pytest.fixture
def sample_dataframe():
    """Provides a sample DataFrame with numeric and missing values."""
    return pd.DataFrame({
        "A": [1, 2, None],
        "B": [4, 5, 6]
    })

@pytest.fixture
def dataframe_with_duplicates():
    """Provides a DataFrame with duplicate columns."""
    return pd.DataFrame({
        "A": [1, 2, 3],
        "A": [4, 5, 6]  # Duplicate column names
    })

@pytest.fixture
def dataframe_with_outliers():
    """Provides a DataFrame with numeric outliers."""
    return pd.DataFrame({
        "A": [1, 2, 100],
        "B": [4, 5, 6]
    })
