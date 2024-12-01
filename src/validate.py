import pandas as pd
from src.config_loader import load_config

# Load validation settings from YAML configuration
config = load_config()

def validate_data(df):
    """
    Validates a DataFrame based on configuration settings.
    
    - Checks for missing values.
    - Checks for duplicate columns.
    - Allows thresholds for missing values.
    """
    # Check for missing values
    if config["validation"]["check_missing_values"]:
        missing_fraction = df.isnull().mean().mean()
        if missing_fraction > config["validation"]["missing_value_threshold"]:
            print(f"Warning: Missing values exceed threshold ({missing_fraction:.2%})")
        elif missing_fraction > 0:
            print(f"Info: Missing values detected ({missing_fraction:.2%})")

    # Check for duplicate columns
    if config["validation"]["check_duplicate_columns"]:
        if not df.columns.is_unique:
            print("Error: Duplicate column names found")

    print("Data validation complete.")
