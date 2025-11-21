import pandas as pd
import os
import sys
import numpy as np
from scipy.stats import chisquare

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

observed = df["Electronics Sales"].values
print(f"Observed Frequency: {observed}")

total_value = observed.sum()
expected = [total_value / 12] * 12
print(f"Expected Frequency: {np.round(expected, 8)}")

chi_stat, p_val = chisquare(observed, expected)

print()
print(f"Chi-square Statistic: {round(chi_stat, 2)}")
print(f"p-value: {p_val}")
print()

if p_val > 0.05:
    print("Fail to")
else:
    print(
        "Reject the null hypothesis. There is not enough evidence to suggest that sales of electronics are evenly distributed across months."
    )
