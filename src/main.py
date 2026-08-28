import pandas as pd

from download import download_data
from clean import clean_data
from validation import automated_validation
from database import load_csv_to_postgres


# Download raw data
print("Downloading data")
download_data()
print("Data downloaded successfully")


# Load raw data
df = pd.read_csv("data/raw/data.csv")


# Clean data
df = clean_data(df)


# Validate cleaned data
errors = automated_validation(df)

if errors:
    print("Validation errors:")
    for error in errors:
        print(f"- {error}")
else:

    df = df[
        [
            "description",
            "title",
            "salary_min",
            "location",
            "longitude",
            "redirect_url",
            "latitude",
            "salary_max",
            "salary_is_predicted",
            "company",
            "id",
            "created",
            "contract_time",
            "contract_type",
            "skills",
            "job_category"
        ]
    ]

    df.to_csv(
        "data/cleaned/data.csv",
        index=False,
        encoding="utf-8"
    )

    print("Cleaned data saved to CSV")


# Load cleaned data into PostgreSQL
load_csv_to_postgres("data/cleaned/data.csv")

print("Data saved to PostgreSQL")