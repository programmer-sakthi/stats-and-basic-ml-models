# **📘 Session 1: Basic Probability Concepts & Terminology**

## ✅ **1. What is Probability?**

Probability measures how likely an event is to occur.

$$
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total possible outcomes}}
$$

Example: Probability of rolling a 4 on a fair die

$$
P(4) = \frac{1}{6}
$$

---

## ✅ **2. Key Terminology**

### **🔹 Experiment**

A process that produces an outcome.  
Example: tossing a coin.

### **🔹 Sample Space (Ω)**

All possible outcomes.  
Example: Ω = {H, T} for a coin toss.

### **🔹 Event**

A subset of the sample space.  
Example: Getting a head, {H}

### **🔹 Equally Likely Outcomes**

All outcomes have the same chance.  
Example: faces of a fair die.

### **🔹 Probability Axioms**

1.  $$
    0 \le P(A) \le 1
    $$

2.  $$
    P(\Omega) = 1
    $$

3.  If A and B are mutually exclusive:
    $$
    P(A \cup B) = P(A) + P(B)
    $$

---

## ✅ **3. Types of Events**

### **🎯 Mutually Exclusive Events**

Cannot occur simultaneously.  
Example: Rolling a 2 and 5 on one die roll.

$$
P(2 \text{ or } 5) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6}
$$

### **🎯 Independent Events**

Occurrence of one event does _not_ affect the other.  
Example: Tossing two coins.

$$
P(\text{H on coin1 and H on coin2}) = \frac{1}{2} \times \frac{1}{2}
$$

### **🎯 Complementary Events**

A and NOT A.

$$
P(A^c) = 1 - P(A)
$$

Example: Not rolling a 6

$$
P(\text{not 6}) = 1 - \frac{1}{6} = \frac{5}{6}
$$

---

# 🐍 **Python Implementation — Session 1**

Let’s implement basic probability using Python.

---

## **⭐ Example 1: Simulating a Coin Toss**

```python
import random

def coin_toss():
    return random.choice(["H", "T"])

# simulate 10 tosses
results = [coin_toss() for _ in range(10)]
results
```

---

## **⭐ Example 2: Estimating Probability by Simulation**

Estimate probability of getting Heads.

```python
import random

def estimate_coin_probability(n=10000):
    outcomes = [random.choice(["H", "T"]) for _ in range(n)]
    return outcomes.count("H") / n

estimate_coin_probability()
```

---

## **⭐ Example 3: Rolling a Die**

```python
import random

def roll_die():
    return random.randint(1, 6)

# simulate 20 rolls
[roll_die() for _ in range(20)]
```

---

## **⭐ Example 4: Estimating P(rolling a 6)**

```python
def estimate_die_probability(target=6, n=10000):
    outcomes = [roll_die() for _ in range(n)]
    return outcomes.count(target) / n

estimate_die_probability()
```
