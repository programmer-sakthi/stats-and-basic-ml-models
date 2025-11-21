import pandas as pd
import os
import sys
from scipy.stats import skew, kurtosis  # WHY SPECIFIC LIBRABY WHY NOT BUILT IN

file1 = input()
file2 = input()

df1 = pd.read_csv(os.path.join(sys.path[0], file1))
df2 = pd.read_csv(os.path.join(sys.path[0], file2))


def statCalc(df):
    data = df["Delivery_Time_Hours"]

    mean = data.mean()
    median = data.median()
    mod = data.mode()
    var = data.var()
    std = data.std()
    ske = skew(data)
    kur = kurtosis(data)

    return {
        "Mean": round(mean, 2),
        "Median": round(median, 2),
        "Mode": round(mod[0], 2),
        "Variance": round(var, 2),
        "Std Dev": round(std, 2),
        "Skewness": round(ske, 3),
        "Kurtosis": round(kur, 3),
    }


if __name__ == "__main__":

    pop_data = statCalc(df1)
    print("Population Stats:")
    print("", pop_data)

    sam_data = statCalc(df2)
    print("Sample Stats:")
    print("", sam_data)
