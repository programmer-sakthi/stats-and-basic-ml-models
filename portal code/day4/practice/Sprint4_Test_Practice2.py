import os
import sys
import pandas as pd
from scipy.stats import chi2_contingency


file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

print("Null Hypothesis (H0): Page Loads are independent of Day of the Week.")
print("Alternative Hypothesis (H1): Page Loads depend on Day of the Week.\n")


df["Page_Loads_Bin"] = pd.qcut(df["Page.Loads"], q=3, labels=["Low", "Medium", "High"])
print(df["Page_Loads_Bin"])


contingency_table = pd.crosstab(df["Day"], df["Page_Loads_Bin"])
print("Contingency Table (Page Loads vs Day of the Week):\n")
print(contingency_table)

chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)
print(f"\nChi-Square Statistic: {chi2_stat:.2f}")
print(f"p-value: {p_val:.4f}")

alpha = 0.05
if p_val < alpha:
    print("\nConclusion: Reject H0. Page Loads depend on the Day of the Week.")
else:
    print(
        "\nConclusion: Fail to reject H0. No significant relationship between Page Loads and Day of the Week."
    )
