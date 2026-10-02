import random as rand
import pandas as pd

def get_sample(df):
    """Print a random sample of 5 rows."""

    limit, columns = df.shape

    random_number = rand.randint(0, limit - 5)

    for i in range(random_number, random_number + 5):
        print(df.iloc[i])
        print("\nNext sample\n")


def get_column_sample(df):
    """Print 10 random values from a selected column."""

    column = input("Which column do you want a sample from? ")

    if column not in df.columns:
        print(f"Column '{column}' not found.")
        return

    limit, columns = df.shape

    random_number = rand.randint(0, limit - 10)

    for i in range(random_number, random_number + 10):
        print(df[column].iloc[i])


def main(df):
    """Run basic exploratory functions."""

    get_sample(df)

    print(df.columns.tolist())

    get_column_sample(df)

data_set = input("Do you want to sample raw or cleaned data")
if data_set.lower() == "raw":
    df = pd.read_csv("data/raw/data.csv")
else:
    df = pd.read_csv("data/cleaned/data.csv")

main(df)