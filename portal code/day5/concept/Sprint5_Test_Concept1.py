import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())

    print("Loan Data Analysis Started.")

    # SECTION 1 : PRINT FIRST 5 ROWS
    print("\nFirst 5 Rows")
    print(df.head())

    # SECTION 2 : PRINT COLUMN NAMES AND SHAPE
    print("Column Names")
    print(df.columns.to_list())
    print("Dataset Shape")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # SECTION 3 : PRINT COLUMN DATATYPES AND NOT NULL COUNT
    print("Column Data Types and Non-Null Counts")
    for column in df.columns:
        datatype = df[column].dtype
        value_count = df[column].notnull().sum()
        print(f"{column:<20} Non-null: {value_count:<3} Type: {datatype}")

    # SECTION 4 : SUMMARY STATISTICS
    print("Summary Statistics")
    print(df.describe())

    # SECTION 5.1 : VALUE COUNTS FOR 'purpose'
    print("Value Counts for 'purpose'")
    print(df["purpose"].value_counts())
    # SECTION 5.2 : VALUE COUNTS FOR 'credit.policy'
    print("Value Counts for 'credit.policy'")
    print(df["credit.policy"].value_counts())
    # SECTION 5.3 : VALUE COUNTS FOR 'not.fully.paid'
    print("Value Counts for 'not.fully.paid'")
    print(df["not.fully.paid"].value_counts())


if __name__ == "__main__":
    compute()
