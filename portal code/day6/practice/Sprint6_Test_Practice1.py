import os
import sys

import pandas as pd
from sklearn.preprocessing import StandardScaler


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():

    df = get_csv(input())
    print("First 5 rows of selected data:")
    req_columns = [
        "Customer_Age",
        "Order_Quantity",
        "Unit_Cost",
        "Unit_Price",
        "Revenue",
    ]
    df = df[req_columns]
    print(df.head())

    print("\nMissing values before treatment:")
    print(df.isnull().sum())

    df = df.fillna(df.mean())

    print("\nMissing values after treatment:")
    print(df.isnull().sum())

    for column in df.columns:
        df[column] = df[column].astype("float")

    # apply outlier treatment using IQR Winsorization
    # capping values outside 1.5 times the IQR to the nearest fence value for each column
    Q1, Q3 = df.quantile(0.25), df.quantile(0.75)
    IQR = Q3 - Q1
    df = df.clip(Q1 - 1.5 * IQR, Q3 + 1.5 * IQR, axis=1)
    print("\nOutlier treatment done. DataFrame with capped outliers:")
    print(df.head())

    scaled = pd.DataFrame(StandardScaler().fit_transform(df), columns=req_columns)

    print("\nFirst 5 rows after scaling:")
    print(scaled.head())

    print("Correlation of features with Revenue (sorted):")
    print(scaled.corr()[["Revenue"]].sort_values(by="Revenue"))


if __name__ == "__main__":
    compute()
