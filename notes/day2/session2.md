# Sampling Distributions

[Sampling Distributions - GFG reference material](https://www.geeksforgeeks.org/maths/sampling-distribution/)

# Standard Error in Sampling Distributions

The **standard error (SE)** in a sampling distribution refers to the standard deviation of the sampling distribution of a sample statistic, most commonly the sample mean. It quantifies the variability or spread of sample means around the population mean.

In simple terms, it tells you how much the sample mean is likely to vary from the true population mean due to random sampling. The smaller the standard error, the more consistent the sample means will be, and the more reliable your estimates of the population parameter (e.g., population mean) will be.

## Formula for Standard Error of the Mean

The standard error of the mean is given by the formula:

$$
SE = \frac{\sigma}{\sqrt{n}}
$$

Where:

- \( \sigma \) = population standard deviation
- \( n \) = sample size

## Key Points:

1. **Larger sample sizes** result in a **smaller standard error**, meaning more precise estimates of the population parameter.
2. If the **population standard deviation** (\( \sigma \)) is known, this formula applies. If it's unknown, you can use the **sample standard deviation** (\( s \)) to estimate the standard error:

   $$
   SE = \frac{s}{\sqrt{n}}
   $$

3. **Central Limit Theorem (CLT)**: As the sample size increases, the sampling distribution of the sample mean will approach a normal distribution, regardless of the shape of the population distribution. This is especially true when the sample size is greater than 30.

## Example:

If you have a population with a standard deviation \( \sigma = 10 \) and you take a sample of size \( n = 25 \), the standard error would be:

$$
SE = \frac{10}{\sqrt{25}} = \frac{10}{5} = 2
$$

So, the standard error of the sample mean is 2. This means that if you repeatedly take samples of size 25 from this population, the sample means will typically vary by about 2 units from the true population mean.

## Why is Standard Error Important?

- **Precision of Estimates**: A smaller standard error means your sample mean is a more precise estimate of the population mean.
- **Confidence Intervals**: Standard error is used to calculate confidence intervals for population parameters. Smaller standard errors lead to narrower intervals, which are more precise.
- **Hypothesis Testing**: It helps in testing hypotheses by determining how much the sample mean deviates from the null hypothesis value.
