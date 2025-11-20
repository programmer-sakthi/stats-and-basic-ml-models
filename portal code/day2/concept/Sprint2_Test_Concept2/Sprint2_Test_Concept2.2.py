import pandas as pd
import numpy as np
import sys
from scipy.stats import skew, kurtosis
import os


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def random_sampling(df, count=50):
    random_df = df.sample(n=count, random_state=42)
    return random_df
    # print(random_df.head().reset_index(drop=True))


def compute():
    filename = input()
    df = get_csv(filename)

    print("File loaded successfully:", filename)
    print("Data shape:", df.shape)
    print("Preview of Loaded Data:")
    print(df.head())

    print("Simple Random Sampling (50 students):")
    sample_data = random_sampling(df)
    print(sample_data.head().reset_index(drop=True))

    print("Summary Statistics of the Population data")
    filtered = df["Height_cm"]
    summary = filtered.describe()
    print(round(summary, 1))
    print(f"median: {filtered.median()} mode: {filtered.mode()[0]}")
    print(f"skewness: {skew(filtered):.3f} kurtosis: {kurtosis(filtered):.3f}")

    print("Summary Statistics of the Sample data")
    filtered = sample_data["Height_cm"]
    summary = filtered.describe()
    print(round(summary, 1))
    print(f"median: {filtered.median()} mode: {filtered.mode()[0]}")
    print(f"skewness: {skew(filtered):.3f} kurtosis: {kurtosis(filtered):.3f}")


if __name__ == "__main__":
    compute()
