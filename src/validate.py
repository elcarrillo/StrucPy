import pandas as pd
import logging
from config_loader import load_config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_data(df):
    """
    Validates a DataFrame based on configuration settings.
    
    - Checks for missing values.
    - Checks for duplicate columns.
    - Detects outliers in numeric columns.
    - Logs warnings and errors based on thresholds.
    - Returns a summary of validation results.
    """
    # Load validation settings from YAML configuration
    config = load_config() or {}
    validation_config = config.get("validation", {})

    # Validation results
    results = {
        "missing_values": False,
        "duplicate_columns": False,
        "outliers": []
    }

    # Check if DataFrame is empty
    if df.empty:
        logger.warning("The DataFrame is empty. Validation skipped.")
        return results

    # Check for missing values
    if validation_config.get("check_missing_values", False):
        missing_fraction = df.isnull().mean().mean()
        threshold = validation_config.get("missing_value_threshold", 0.1)
        if missing_fraction > threshold:
            logger.warning(f"Missing values exceed threshold ({missing_fraction:.2%})")
            results["missing_values"] = True
        elif missing_fraction > 0:
            logger.info(f"Missing values detected ({missing_fraction:.2%})")

    # Check for duplicate columns
    if validation_config.get("check_duplicate_columns", False):
        if not df.columns.is_unique:
            logger.error("Duplicate column names found")
            results["duplicate_columns"] = True

    # Check for outliers
    if validation_config.get("check_outliers", False):
        for column in df.select_dtypes(include=['number']).columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
            if not outliers.empty:
                logger.warning(f"Outliers detected in column '{column}'")
                results["outliers"].append(column)

    logger.info("Data validation complete.")
    return results
