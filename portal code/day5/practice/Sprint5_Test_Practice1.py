import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input("Enter the CSV file name (e.g., income_data.csv): "))
    df.replace(
        "?", "Unknown", inplace=True
    )  # in output ? is mentioned as Unknown while using value counts

    # SECTION 1 : PRINT FIRST 5 ROWS
    print("First 5 Rows:")
    print(df.head())

    # SECTION 2 : PRINT COLUMN NAMES AND SHAPE
    print("\nColumn Names:")
    print(df.columns.to_list())
    print("\nDataset Shape:")
    print(f"\nRows: {df.shape[0]}, Columns: {df.shape[1]}")

    # SECTION 3 : PRINT COLUMN DATA TYPES AND NON NULL COUNTS
    print("\nColumn Data Types and Non-Null Counts:")
    for column in df.columns:
        data_type = df[column].dtype
        non_null = df[column].notnull().sum()
        print(f"{column:<25} Non-Null: {non_null:<7} Type: {data_type}")

    # SECTION 4 : PRINT SUMMARY STATISTICS
    print("\nSummary Statistics (Numerical Columns):")
    print(df.describe())

    # SECTION 5 : CATEGORIAL COLUMNS AND VALUE COUNTS
    print("\nCategorical Columns and Value Counts:")

    columns_to_print = [
        "WorkClass",
        "Education",
        "Marital_Status",
        "Occupation",
        "Relationship",
        "Gender",
        "Native_Country",
        "Income_Bracket",
    ]
    for column in columns_to_print:
        print(f"\nColumn: {column}")
        print(df[column].value_counts())

    print("\nGender Distribution:")
    column = "Gender"
    print(df[column].value_counts())


if __name__ == "__main__":
    compute()
