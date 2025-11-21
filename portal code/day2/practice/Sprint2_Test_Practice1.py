import os
import sys
import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    print("File loaded successfully:", file)
    return pd.read_csv(path)


def preview_data(df):
    print("Data shape:", df.shape)
    print()
    print("Preview of Loaded Data:")
    print(df.head())


def random_sampling(df):
    sample = df.sample(n=50, random_state=42)
    print()
    print("1.1: Simple Random Sample of 50 deliveries:")
    print(sample.head().reset_index(drop=True))
    print()


def stratified_sampling(df):
    print()
    print("1.2: Stratified Sample by Zone (proportional to dataset):")
    largest_zone = df["Zone"].value_counts().idxmax()
    sample = df[df["Zone"] == largest_zone].sample(5, random_state=42)
    print(sample.head().reset_index(drop=True))


def systematic_sampling(df):
    print()
    print("1.3: Systematic Sample (every 10th order):")
    sample = df.iloc[::10]
    print(sample.head().reset_index(drop=True))


def compute():
    df = get_csv(input("Enter the dataset filename (with .csv or .xlsx extension):"))
    preview_data(df)
    random_sampling(df)
    stratified_sampling(df)
    systematic_sampling(df)


if __name__ == "__main__":
    compute()
