import pandas as pd
import os
import sys
import numpy as np
from scipy.stats import chisquare

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

print(
    f"Null Hypothesis (H0): First-Time Visits are equally distributed across days of the month."
)
print(
    f"Alternative Hypothesis (H1): First-Time Visits are not equally distributed across days of the month."
)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["DayOfMonth"] = df["Date"].dt.day
observed = df.groupby("DayOfMonth")["First.Time.Visits"].sum().values

print()
print("Observed Frequencies (First-Time Visits per Day):")
print(observed)

total_observed = observed.sum()
num = len(observed)
expected = [total_observed / num] * num

print()
print("Expected Frequencies (assuming equal distribution): ")
print(np.round(expected, 8))
print()

chi_val, p_val = chisquare(observed, expected)
print(f"Chi-Square Statistic: {round(chi_val, 2)}")
print(f"p-value: {p_val}")
print()

if p_val < 0.05:
    print(
        "Conclusion: Reject H0. First-Time Visits are not equally distributed across days of the month."
    )
