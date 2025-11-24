# 📘 Sampling Distributions – Complete Notes

[Video Reference](https://www.youtube.com/watch?v=7S7j75d3GM4)

---

# 1. What is a Sampling Distribution?

A **sampling distribution** is the probability distribution of a **statistic** (mean, median, proportion, etc.) calculated from **many repeated samples** of the same population.

It shows **how the statistic varies** from sample to sample and forms the basis of **inferential statistics**.

- Helps estimate population parameters
- Measures variability of statistics
- Foundation for confidence intervals & hypothesis testing

---

# 2. Important Terminologies

## 1. Statistic

**Analogy:** Tasting one spoon of sambhar to guess the pot’s taste.  
**Meaning:** A numerical value computed from a sample.  
**Example:** Mean height of 50 students = 165 cm.

---

## 2. Parameter

**Analogy:** The actual taste of the entire sambhar pot.  
**Meaning:** A numerical value describing the full population.  
**Example:** True average height of 5,000 students = 167 cm.

---

## 3. Sample

**Analogy:** A spoon taken from the pot.  
**Meaning:** A subset of the population.

---

## 4. Population

**Analogy:** The entire pot of sambhar.  
**Meaning:** The full group you want to study.

---

## 5. Sampling Distribution

**Analogy:** If you take many spoons from different areas, each spoon tastes slightly different.  
Plotting all these tastes gives a sampling distribution.

**Meaning:** The distribution of a statistic when many samples are taken repeatedly.

---

## 6. Central Limit Theorem (CLT)

**Analogy:** Even if the sambhar tastes uneven, large spoonfuls average out and taste normal.

**Meaning:** For sufficiently large sample sizes (n ≥ 30), the distribution of sample means becomes **approximately normal** even if the population is not.

---

## 7. Standard Error (SE)

**Analogy:** How much the taste changes from spoon to spoon.  
**Meaning:** Standard deviation of the sampling distribution.

---

## 8. Bias

**Analogy:** If you always take spoons from the oily top, your judgement is skewed.  
**Meaning:** Systematic error that pushes your estimate away from truth.

---

## 9. Confidence Interval (CI)

**Analogy:** “I am 95% sure the salt is within this range.”  
**Meaning:** Range likely to include the true population parameter.

---

## 10. Sampling Methods

- **Random Sampling:** Dip the spoon anywhere
- **Stratified Sampling:** Take from every layer
- **Systematic Sampling:** Every 5th spoon

---

## 11. Inferential Statistics

**Analogy:** Tasting one spoon to judge the whole pot.  
**Meaning:** Using sample data to make population conclusions.

---

## 12. Hypothesis Testing

**Analogy:** Checking if the chef’s claim “sambhar is perfect” is correct.  
**Meaning:** Testing assumptions about population using sample data.

---

# 3. Key Characteristics of Sampling Distributions

## 1. Mean of Sampling Distribution

$$
\
\mu_{\bar{x}} = \mu
\
$$

Sample means center around the population mean.

---

## 2. Variance of Sampling Distribution

$$
\
\text{Var}(\bar{X}) = \frac{\sigma^2}{n}
\
$$

Larger sample size → smaller variance → more stable estimates.

---

![Population Distribution vs Sampling Distribution](./resources/population%20distribution%20vs%20sampling%20distribution.png)

---

# 4. Standard Error (SE)

The **standard error** is the standard deviation of the sampling distribution of a statistic.

### Formula

$$
\
SE = \frac{\sigma}{\sqrt{n}}
\
$$

If σ is unknown:

$$
\
SE = \frac{s}{\sqrt{n}}
\
$$

### Key Points

- Larger sample size → smaller SE
- Used for confidence intervals
- Used in hypothesis testing
- Under CLT, SE helps form normal sampling distributions

### Example

Population SD $\sigma = 10$, sample size \( n = 25 \):

$$
\
SE = \frac{10}{5} = 2
\
$$

So sample means vary roughly ±2 around the true mean.

---

# 5. Importance of Standard Error

- Measures precision of the sample mean
- Smaller SE → more reliable estimates
- Used in building confidence intervals
- Used in hypothesis testing

---
