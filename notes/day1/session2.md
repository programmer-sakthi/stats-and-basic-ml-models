# **📘 Session 2: Joint Probability**

## ✅ **1. What is Joint Probability?**

Joint probability measures the likelihood of **two events happening together**.

$$
P(A \cap B)
$$

This represents “Probability of A **and** B happening”.

---

## ✅ **2. Joint Probability for Independent Events**

If events do **not** affect each other:

$$
P(A \cap B) = P(A) \times P(B)
$$

### **Example**

Event A: Get Heads on a coin toss → \(P(A) = \frac{1}{2}\)  
Event B: Roll a 4 on a die → \(P(B) = \frac{1}{6}\)

$$
P(A \cap B) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12}
$$

---

## ✅ **3. Joint Probability for Dependent Events**

If the outcome of the first event affects the second:

$$
P(A \cap B) = P(A) \times P(B|A)
$$

### **Example: Drawing Cards**

Total aces = 4  
Total cards = 52

Step 1: Probability first card is an Ace:

$$
P(A) = \frac{4}{52}
$$

Step 2: After drawing one Ace:

Remaining aces = 3  
Remaining cards = 51

$$
P(B|A) = \frac{3}{51}
$$

Joint probability:

$$
P(A \cap B) = \frac{4}{52} \times \frac{3}{51}
$$

---

## ✅ **4. General Joint Probability Formula**

For any two events A and B:

$$
P(A \cap B) = P(A) \cdot P(B|A)
$$

or:

$$
P(A \cap B) = P(B) \cdot P(A|B)
$$

---

# 🐍 **Python Implementation — Session 2**

---

## ⭐ **Example 1: Joint Probability (Independent Events)**

Simulating coin toss + die roll.

```python
import random

def coin():
    return random.choice(["H", "T"])

def die():
    return random.randint(1, 6)

def simulate_joint_independent(n=10000):
    count = 0
    for _ in range(n):
        if coin() == "H" and die() == 4:
            count += 1
    return count / n

simulate_joint_independent()
```

---

## ⭐ **Example 2: Joint Probability (Dependent Events)**

Drawing 2 cards without replacement.

```python
import random

def draw_two_cards_simulation(n=10000):
    count = 0
    for _ in range(n):
        deck = ["A"]*4 + ["N"]*48
        random.shuffle(deck)

        first = deck.pop(0)
        second = deck.pop(0)

        if first == "A" and second == "A":
            count += 1

    return count / n

draw_two_cards_simulation()
```

---

## ⭐ **Example 3: Joint Probability Using Formula**

```python
P_A = 4/52          # first Ace
P_B_given_A = 3/51   # second Ace given first was Ace

P_joint = P_A * P_B_given_A
P_joint
```

---
