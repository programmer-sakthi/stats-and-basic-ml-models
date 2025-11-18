# **Session 1: Basic Probability Concepts & Terminology**

## **1.1 Probability of Single Events (Basic Probability)**

**Example:** Probability of getting heads on a fair coin.

```python
# Probability of an event A (e.g., getting heads on a fair coin)

p_heads = 0.5          # Probability of heads on a fair coin
p_tails = 1 - p_heads  # Probability of tails

print(f"Probability of heads: {p_heads}")
print(f"Probability of tails: {p_tails}")
```

---

## **1.2 Probability of Multiple Independent Events (Multiplication Rule)**

**Example:**

- Event A: Getting heads on a fair coin → P(A) = 0.5
- Event B: Rolling a 4 on a fair die → P(B) = 1/6

```python
# Probability of multiple independent events

p_heads = 0.5
p_4_on_die = 1/6

# Probability of both events happening
p_both_events = p_heads * p_4_on_die
print(f"Probability of both events happening: {p_both_events}")
```

---

# **Session 2: Joint Probability with Examples**

## **2.1 Joint Probability (Independent Events)**

```python
# Joint probability of independent events

p_A = 0.5  # Probability of event A
p_B = 0.6  # Probability of event B

# Joint probability P(A and B) = P(A) * P(B)
joint_probability = p_A * p_B
print(f"Joint probability of A and B: {joint_probability}")
```

---

## **2.2 Joint Probability (Dependent Events)**

Example: Drawing two cards from a deck **without replacement**

```python
# Joint probability of dependent events (drawing 2 Aces)

p_A = 4/52     # Probability first card is an Ace
p_B_given_A = 3/51  # Probability second card is an Ace given the first was an Ace

joint_probability_dependent = p_A * p_B_given_A
print(f"Joint probability of drawing 2 Aces: {joint_probability_dependent}")
```

---

# **Session 3: Conditional Probability & Bayes' Theorem**

## **3.1 Conditional Probability**

We use:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

Example: Probability a light bulb is defective **given** the test is positive.

```python
# Conditional probability P(Defective | Test Positive)

P_defective = 0.02
P_test_positive_given_defective = 0.9
P_test_positive_given_good = 0.05
P_good = 1 - P_defective

# Total probability of a positive test
P_test_positive = (
    P_test_positive_given_defective * P_defective
    + P_test_positive_given_good * P_good
)

# Conditional probability using Bayes' rule
P_defective_given_test_positive = (
    P_test_positive_given_defective * P_defective
) / P_test_positive

print(f"Conditional Probability of Defective given Test Positive: {P_defective_given_test_positive}")
```

---

## **3.2 Bayes' Theorem**

Bayes’ theorem:

$$
P(D|T) = \frac{P(T|D)P(D)}{P(T)}
$$

Example: Chance a patient actually has a disease given a positive test.

```python
P_disease = 0.01
P_positive_given_disease = 0.95
P_positive_given_no_disease = 0.05
P_no_disease = 1 - P_disease

# Total probability of positive test
P_positive = (
    P_positive_given_disease * P_disease
    + P_positive_given_no_disease * P_no_disease
)

# Bayes' Theorem
P_disease_given_positive = (
    P_positive_given_disease * P_disease
) / P_positive

print(f"Probability of Disease given Positive Test: {P_disease_given_positive}")
```
