# **📘 Session 3: Conditional Probability & Bayes’ Theorem**

## ✅ **1. What is Conditional Probability?**

Conditional probability is the probability of an event **given** that another event has already occurred.

For two events \(A\) and \(B\), the **conditional probability** of \(A\) given \(B\) is:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

### **Example: Drawing Cards**

Let’s say event \(A\) is drawing a red card, and event \(B\) is drawing a face card (Jack, Queen, or King). The probability of drawing a red face card can be calculated using conditional probability.

- Total red cards = 26
- Total face cards = 12
- Red face cards = 6

The probability of drawing a red card, given that you drew a face card, is:

$$
P(\text{Red}|\text{Face}) = \frac{6}{12} = \frac{1}{2}
$$

---

## ✅ **2. Bayes' Theorem**

Bayes' Theorem is a way to reverse conditional probabilities.
It allows us to update the probability of an event based on new evidence.

The formula for Bayes’ Theorem is:

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

Where:

- \(P(A|B)\) = Posterior probability (updated probability of \(A\) given \(B\))
- \(P(B|A)\) = Likelihood (probability of \(B\) given \(A\))
- \(P(A)\) = Prior probability (initial probability of \(A\))
- \(P(B)\) = Evidence (probability of \(B\))

### **Example: Medical Test**

Consider a medical test for a disease:

- **Prior probability**: The probability of a person having the disease is
  $$ P(\text{Disease}) = 0.01 $$

- **Likelihood**: The probability of testing positive given that the person has the disease is
  $$ P(\text{Positive} | \text{Disease}) = 0.95 $$

- **Evidence**: The probability of testing positive, regardless of whether the person has the disease, is
  $$ P(\text{Positive}) = 0.05 $$

We want to know the probability that a person has the disease, given that they tested positive:

$$
P(\text{Disease}|\text{Positive}) = \frac{P(\text{Positive}|\text{Disease}) \cdot P(\text{Disease})}{P(\text{Positive})}
$$

Substitute the values:

$$
P(\text{Disease}|\text{Positive}) = \frac{0.95 \times 0.01}{0.05} = 0.19
$$

So, even with a positive test result, the probability that the person has the disease is only 19%, due to the low prior probability of the disease.

---

## ✅ **3. Applying Bayes' Theorem in Practice**

### **Example: Email Spam Classification**

Let’s apply Bayes’ Theorem to classify emails as "Spam" or "Not Spam".

- **Prior probability** $$P(\text{Spam}) = 0.2$$
- **Likelihood** $$P(\text{Word|Spam}) = 0.4$$ (probability of the word "Buy" in a spam email)
- **Evidence** $$P(\text{Word}) = 0.3$$ (probability of the word "Buy" in any email)

We want to know the probability that an email is spam, given that it contains the word "Buy":

$$
P(\text{Spam}|\text{Word}) = \frac{P(\text{Word}|\text{Spam}) \cdot P(\text{Spam})}{P(\text{Word})}
$$

Substitute the values:

$$
P(\text{Spam}|\text{Word}) = \frac{0.4 \times 0.2}{0.3} \approx 0.267
$$

So, the probability that the email is spam, given that it contains the word "Buy", is approximately **26.7%**.

---

# 🐍 **Python Implementation — Session 3**

Now let’s implement **Conditional Probability** and **Bayes' Theorem** in Python.

---

## ⭐ **Example 1: Conditional Probability (Drawing Cards)**

```python
def conditional_probability_red_given_face():
    total_red_cards = 26
    total_face_cards = 12
    red_face_cards = 6

    return red_face_cards / total_face_cards

conditional_probability_red_given_face()
```

---

## ⭐ **Example 2: Bayes' Theorem (Medical Test)**

```python
def bayes_theorem_medical_test():
    # Prior probability: probability of having the disease
    P_disease = 0.01
    # Likelihood: probability of testing positive given disease
    P_positive_given_disease = 0.95
    # Evidence: probability of testing positive
    P_positive = 0.05

    # Bayes' theorem formula
    P_disease_given_positive = (P_positive_given_disease * P_disease) / P_positive

    return P_disease_given_positive

bayes_theorem_medical_test()
```

---

## ⭐ **Example 3: Bayes' Theorem (Email Spam)**

```python
def bayes_theorem_spam_email():
    # Prior probability of spam
    P_spam = 0.2
    # Likelihood: probability of the word "Buy" given spam
    P_word_given_spam = 0.4
    # Evidence: probability of the word "Buy"
    P_word = 0.3

    # Bayes' theorem formula
    P_spam_given_word = (P_word_given_spam * P_spam) / P_word

    return P_spam_given_word

bayes_theorem_spam_email()
```

---
