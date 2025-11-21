import pandas as pd
import os
import sys
from scipy.stats import chi2_contingency

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

table = df[["Electronics", "Clothing", "Home Goods"]].values

print(f"Contingency Table (Observed Frequencies):\n {table}")

chi_val, p_val, dof, expe = chi2_contingency(table)

print()
print(f"Chi-Square Statistic: {round(chi_val, 2)}")
print(f"Degrees of Freedom: {dof}")
print(f"P-Value: {p_val:.1f}")
print()

data = pd.DataFrame(
    expe, index=df["Quarter"], columns=["Electronics", "Clothing", "Home Goods"]
)
data.index.name = None
print("Expected Frequencies:")
print(data)
print()

if p_val < 0.05:
    print("Reject the null hypothesis.")
    print(
        "There is enough evidence to suggest that the distribution of sales is different across the four quarters."
    )
