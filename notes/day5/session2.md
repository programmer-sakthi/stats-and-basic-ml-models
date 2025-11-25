# Session 2 — Encoding Categorical Variables

## Data preprocessing (Machine Learning)

Categorical variables represent labels, groups, or classes (e.g., color, size, city). Most ML models require numerical inputs, so categorical data must be encoded into numbers. Proper encoding helps models interpret these features and improves predictive performance.

## Key encoding types

- Label Encoding
- One-Hot Encoding
- Ordinal Encoding
- Binary Encoding
- Target Encoding

## Categorical data types

- Ordinal data: categories with a meaningful order (e.g., Small < Medium < Large).
- Nominal data: categories without any order (e.g., Red, Blue, Green).

---

## 1. Label Encoding

Label encoding maps each category to a unique integer. It's simple and memory-efficient but can introduce an implicit order where none exists (problematic for nominal features).

Example — Column: Size  
Categories: Small, Medium, Large  
Label encoded: 0, 1, 2

Advantages:

- Simple and fast
- Works well with tree-based models

Disadvantages:

- May unintentionally introduce ordinal relationships (bad for non-ordinal data)

Code (sklearn):

```python
from sklearn.preprocessing import LabelEncoder

categories = ['Small', 'Medium', 'Large']
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(categories)
print(encoded_labels)  # [0 1 2]
```

---

## 2. One-Hot Encoding

One-hot encoding creates a binary column for each category. Use for nominal data to avoid introducing order.

Example — Column: Color  
Categories: Red, Blue, Green

One-hot encoded:

- Red -> [1, 0, 0]
- Blue -> [0, 1, 0]
- Green-> [0, 0, 1]

Advantages:

- Avoids ordinal assumptions
- Clear interpretability

Disadvantages:

- High dimensionality for many unique categories ("curse of dimensionality")

Code (pandas):

```python
import pandas as pd

df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Red']})
encoded = pd.get_dummies(df, columns=['Color'])
print(encoded)
#    Color_Blue  Color_Green  Color_Red
# 0           0            0          1
# 1           1            0          0
# 2           0            1          0
# 3           0            0          1
```

---

## 3. Ordinal Encoding

Ordinal encoding maps categories to integers while preserving a known order (e.g., ratings or sizes). Only use when the order is meaningful.

Example — Column: Size  
Categories (ordered): Small, Medium, Large  
Ordinal encoded: 0, 1, 2

Advantages:

- Preserves order
- Simple

Disadvantages:

- Not suitable for nominal features (introduces artificial order)

Code (sklearn):

```python
from sklearn.preprocessing import OrdinalEncoder

sizes = [['Small'], ['Medium'], ['Large']]
ordinal_encoder = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])
encoded_sizes = ordinal_encoder.fit_transform(sizes)
print(encoded_sizes)
# [[0.]
#  [1.]
#  [2.]]
```

---

## 4. Binary Encoding

Binary encoding is useful for high-cardinality categorical features. It assigns an integer to each category (like label encoding), converts to binary, and splits binary digits into several columns.

How it works:

1. Assign a unique integer to each category.
2. Convert each integer to binary.
3. Use binary digits as columns.

Example — Color with 5 categories:

- Red -> 0 -> 000
- Green -> 1 -> 001
- Blue -> 2 -> 010
- Yellow -> 3 -> 011
- Black -> 4 -> 100

Resulting columns (Bin_1, Bin_2, Bin_3):

```
Color   Bin_1  Bin_2  Bin_3
Red       0      0      0
Green     0      0      1
Blue      0      1      0
Yellow    0      1      1
Black     1      0      0
```

Advantages:

- Compact representation for high-cardinality features
- Reduces sparsity vs one-hot encoding

Disadvantages:

- Binary codes can imply order or relationships not meaningful to the feature
- Less intuitive to interpret

Code (category_encoders):

```python
import pandas as pd
import category_encoders as ce

df = pd.DataFrame({'Color': ['Red', 'Green', 'Blue', 'Yellow', 'Black']})
encoder = ce.BinaryEncoder(cols=['Color'])
df_encoded = encoder.fit_transform(df)
print(df_encoded)
#    Color_0  Color_1  Color_2
# 0        0        0        0
# 1        0        0        1
# 2        0        1        0
# 3        0        1        1
# 4        1        0        0
```

---

## Notes on choosing an encoder

- Use one-hot for low-cardinality nominal features.
- Use ordinal encoding when categories have a true order.
- Use binary or target encoding for high-cardinality features when you need fewer columns.
- Always be cautious about introducing unintended order or leakage (especially with target encoding).
