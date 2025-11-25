import os
import sys

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(
        input(
            "Enter the CSV file name (e.g., income_data.csv): Initial missing values per column:"
        )
    )
    print()
    print(df.isnull().sum())

    print("\nMissing values per column after replacing ' ?' with NaN:")
    df.replace(" ?", np.nan, inplace=True)
    print(df.isnull().sum())

    print("\nMissing values per column after filling with mode:")
    df = df.apply(lambda column: column.fillna(column.mode()[0]), axis=0)
    print(df.isnull().sum())

    print("\nData types after conversion  to categorical:")
    change_columns = [
        "WorkClass",
        "Education",
        "Occupation",
        "Relationship",
        "Gender",
        "Native_Country",
        "Income_Bracket",
    ]
    for col in change_columns:
        df[col] = df[col].astype("category")
    print(df.dtypes)

    encoder = LabelEncoder()

    for col in df.select_dtypes(include="category").columns:
        if col != "Income_Bracket":
            df[col + "_encode"] = encoder.fit_transform(df[col])

    print("\nFirst 5 rows of the processed dataframe:")
    print(df.head())


if __name__ == "__main__":
    compute()
