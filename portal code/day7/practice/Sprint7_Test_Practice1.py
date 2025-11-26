import pandas as pd
import os
import sys
from sklearn.preprocessing import StandardScaler

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))
print("First 5 Rows:")
print(df.head())
print()

print("Dataset Info:")
print(df.info())
print()

print("Missing Values:")
print(df.isnull().sum())
print()

df = df.fillna(df.mean())

for col in df.select_dtypes(include="number").columns:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper)

print("Outlier treatment (IQR Winsorization) done.")
print()

scaler = StandardScaler()
scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("First 5 Rows After Scaling:")
print(scaled.head())
print()


corrmatrix = df.corr().abs()
corr = corrmatrix >= 0.7
print("Correlation matrix (absolute values >= 0.7):")
print(corr)
print()

print("Features sorted by absolute correlation with 'PremiumPrice':")
premium = corrmatrix["PremiumPrice"].sort_values(ascending=True).to_frame()
print(premium)
