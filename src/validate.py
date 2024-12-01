import pandas as pd
import logging
from config_loader import load_config  

# Load validation settings from YAML configuration
config = load_config()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def validate_data(df):
    """
    Validates a DataFrame based on configuration settings.
    
    - Checks for missing values.
    - Checks for duplicate columns.
    - Detects outliers in numeric columns.
    - Logs warnings and errors based on thresholds.
    
    Returns:
        dict: Summary of validation results.
    """
    # Initialize validation results
    results = {
        "missing_values": None,
        "duplicates": False,
        "outliers": {}
    }
    
    # Check for missing values
    if config["validation"].get("check_missing_values", True):
        missing_fraction = df.isnull().mean().mean()
        results["missing_values"] = missing_fraction
        if missing_fraction > config["validation"].get("missing_value_threshold", 0.1):
            logging.warning(f"Missing values exceed threshold ({missing_fraction:.2%})")
        elif missing_fraction > 0:
            logging.info(f"Missing values detected ({missing_fraction:.2%})")

    # Check for duplicate columns
    if config["validation"].get("check_duplicate_columns", True):
        if not df.columns.is_unique:
            logging.error("Duplicate column names found")
            results["duplicates"] = True

    # Check for outliers
    if config["validation"].get("check_outliers", True):
        for column in df.select_dtypes(include=["number"]).columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
            if not outliers.empty:
                logging.warning(f"Outliers detected in column '{column}'")
                results["outliers"][column] = outliers.index.tolist()

    logging.info("Data validation complete.")
    return results
