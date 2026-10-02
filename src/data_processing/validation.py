import pandas as pd
from pandas.api.types import (
    is_bool_dtype,
    is_float_dtype,
    is_object_dtype,
    is_string_dtype
)


def checkNull(df):
    """Check that only latitude and longitude contain null values."""

    errors = []

    null_columns = df.columns[df.isna().any()].tolist()

    if 'latitude' not in null_columns or 'longitude' not in null_columns:
        errors.append(f"Unexpected list of null values: {null_columns}")

    return errors


def check_rounding(df):
    """Check latitude and longitude are rounded to 2 decimal places."""

    errors = []

    if not df['longitude'].equals(round(df['longitude'], 2)):
        errors.append("Longitude not rounded to 2dp")

    if not df['latitude'].equals(round(df['latitude'], 2)):
        errors.append("Latitude not rounded to 2dp")

    return errors


def schema_validations(df):
    """Check that important columns have the correct data types."""

    errors = []

    data_mappings = {
        'company': "str",
        'location': "str",
        'salary_is_predicted': "boolean",
        'skills': "list",
        'latitude': "float",
        'longitude': "float"
    }

    for column, expected_type in data_mappings.items():

        if expected_type == "boolean":
            if not is_bool_dtype(df[column]):
                errors.append(column)

        elif expected_type == "str":
            if not is_string_dtype(df[column]):
                errors.append(column)

        elif expected_type == "list":
            if not is_object_dtype(df[column]):
                errors.append(column)

        elif expected_type == "float":
            if not is_float_dtype(df[column]):
                errors.append(column)

    return errors


def check_columns(df):
    """Check unnecessary columns have been removed and new columns exist."""

    errors = []

    columns = df.columns.tolist()

    if 'category' in columns:
        errors.append("Category was not deleted")

    if '__CLASS__' in columns:
        errors.append("__CLASS__ was not deleted")

    if 'adref' in columns:
        errors.append("adref was not deleted")

    if 'skills' not in columns:
        errors.append("Skills not found")

    return errors


def automated_validation(df):
    """Run all validation checks."""

    errors = []

    errors.extend(check_columns(df))
    errors.extend(checkNull(df))
    errors.extend(schema_validations(df))
    errors.extend(check_rounding(df))

    return errors