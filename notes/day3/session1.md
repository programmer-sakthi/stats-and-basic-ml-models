# Hypothesis Testing

> Concise guide to hypothesis testing, when to use parametric vs nonparametric tests, and a worked example.

## Table of contents

- [Hypothesis Testing](#hypothesis-testing)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
  - [Hypotheses](#hypotheses)
  - [Steps in Hypothesis Testing](#steps-in-hypothesis-testing)
  - [Worked example — New drug vs placebo](#worked-example--new-drug-vs-placebo)
  - [Interpreting p-values and decisions](#interpreting-p-values-and-decisions)
  - [Parametric vs Nonparametric Tests](#parametric-vs-nonparametric-tests)
  - [References](#references)

---

## Overview

Hypothesis testing is a statistical procedure used to decide whether the evidence in a sample supports a specific claim about a population parameter.<br>
[Hypothesis Testing and important terms - GFG](https://www.geeksforgeeks.org/software-testing/understanding-hypothesis-testing/)

---

## Hypotheses

- Null hypothesis (H₀): The default assumption; no effect or no difference.
- Alternative hypothesis (H₁ or Ha): Contradicts H₀; indicates an effect or difference.

Example notation:

- H₀: μ₁ = μ₂
- H₁: μ₁ ≠ μ₂

---

## Steps in Hypothesis Testing

1. State H₀ and H₁.
2. Choose significance level α (commonly 0.05).
3. Collect sample data.
4. Compute test statistic and p-value (e.g., t-test for means).
5. Compare p-value to α and make a decision:
   - If p-value ≤ α → reject H₀.
   - If p-value > α → fail to reject H₀.
6. Report conclusion in context.

> Note: "Fail to reject H₀" is not the same as "accept H₀" — it means insufficient evidence to reject.

---

## Worked example — New drug vs placebo

Scenario:

- Drug group (n₁ = 50): mean reduction = 5 mmHg
- Placebo group (n₂ = 50): mean reduction = 3 mmHg
- Significance level: α = 0.05

Perform an independent two-sample t-test. If the computed p-value = 0.02:

- 0.02 < 0.05 → reject H₀ → conclude the drug shows a statistically significant difference.

If p-value = 0.12:

- 0.12 > 0.05 → fail to reject H₀ → no sufficient evidence of a difference.

Optional: quick Python (scipy) example

```python
# filepath: d:\College\5th sem\Professional Electives\Statistical Methods and ML models\notes\day3\session1.md
import numpy as np
from scipy import stats

# sample means / simulated sample data (example)
drug = np.random.normal(loc=5, scale=8, size=50)
placebo = np.random.normal(loc=3, scale=8, size=50)

t_stat, p_val = stats.ttest_ind(drug, placebo)
print(f"t = {t_stat:.3f}, p = {p_val:.3f}")
```

---

## Interpreting p-values and decisions

- p-value: probability of observing the data (or more extreme) assuming H₀ is true.
- Small p-value (commonly < 0.05) → evidence against H₀.
- Always report effect size and confidence intervals along with p-values to show practical significance.

---

## Parametric vs Nonparametric Tests

| Feature         |                                                 Parametric | Nonparametric                                                     |
| --------------- | ---------------------------------------------------------: | ----------------------------------------------------------------- |
| Assumptions     |        Distributional (often normal), interval/ratio scale | Fewer/no distributional assumptions; works with ordinal/nominal   |
| Central measure |                                                       Mean | Median or ranks                                                   |
| Sensitivity     | More powerful when assumptions hold; sensitive to outliers | Robust to outliers; suitable for small samples or non-normal data |
| Examples        |                        t-test, z-test, Pearson correlation | Mann–Whitney U, Wilcoxon, Kruskal–Wallis, Spearman correlation    |
| When to use     |                         Large sample, normally distributed | Small sample, skewed data, ordinal variables                      |

---

## References

- GeeksforGeeks — Understanding Hypothesis Testing: https://www.geeksforgeeks.org/software-testing/understanding-hypothesis-testing/
