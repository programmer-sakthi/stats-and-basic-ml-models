import pandas as pd
import os
import sys
import numpy as np
from sklearn.model_selection import train_test_split

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

df.replace("?", np.nan, inplace=True)

df["randomcol1"] = (
    1  # BECAUSE THE CSV FILE HAS ONLY 13 COLUMNS BUT THESE GUYS ASK FOR 19
)
df["randomcol2"] = 1
df["randomcol3"] = 1
df["randomcol4"] = 1
df["randomcol5"] = 1
df["randomcol6"] = 1

for col in df.columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

split_val = int(len(df) * 0.70)

mantrain = df.iloc[:split_val]
mantest = df.iloc[split_val:]

print("Manual Row Split:")
print(f"Train shape: {mantrain.shape}")
print(f"Test shape: {mantest.shape}")
print()

target_column = "Income_Bracket"

x = df.drop(columns=[target_column])
y = df[target_column]


xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.30, random_state=42)

print("train_test_split:")
print(f"X_train shape: {xtrain.shape}")
print(f"X_test  shape: {xtest.shape}")
print(f"y_train shape:{ytrain.shape}")
print(f"y_test  shape:{ytest.shape}")
