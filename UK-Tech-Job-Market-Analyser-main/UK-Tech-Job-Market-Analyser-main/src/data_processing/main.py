import pandas as pd

from download import download_data
from clean import clean_data
from validation import automated_validation
from database import load_csv_to_postgres


# download raw data
print("downloading data")
download_data()
print("data downloaded successfully")


# load raw data
df = pd.read_csv("data/raw/data.csv")


# clean data
df = clean_data(df)


# validate cleaned data
errors = automated_validation(df)

if errors:
    print("Validation errors:")
    for error in errors:
        print(f"{error}")
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
            "contract_time",
            "contract_type",
            "skills",
            "job_category",
            "location_region",
            "average_salary",
            "created_month",
            "created_year"
        ]
    ]

    df.to_csv(
        "data/cleaned/data.csv",
        index=False,
        encoding="utf-8"
    )

    print("Cleaned data saved to CSV")



# loda cleaned data into postgreSQL
load_csv_to_postgres("data/cleaned/data.csv")

print("data saved to postgreSQL")