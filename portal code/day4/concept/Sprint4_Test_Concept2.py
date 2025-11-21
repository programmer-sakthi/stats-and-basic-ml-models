import pandas as pd
import os
import sys
from scipy.stats import chi2_contingency

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

observed = df[["Electronics Sales", "Clothing Sales", "Home Goods Sales"]].values
print(f"Contingency Table (Observed Frequencies):\n {observed}")

chi_val, p_val, dof, expected = chi2_contingency(observed)

print()
print(f"Chi-square Statistic: {chi_val:.2f}")
print(f"p-value: {p_val}")
print(f"Degrees of Freedom: {dof}")

print()
print(f"Expected Frequencies:\n {expected}")
print()

if p_val < 0.01:
    print("Reject the null hypothesis.")
    print(
        "There is enough evidence to suggest that product sales depend on months (they are related)."
    )
