import pandas as pd
import os
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

reqcol = ['Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Revenue']
data = df[reqcol].copy()

for col in data.columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

for col in data.columns:
    data[col] = data[col].fillna(data[col].mean())

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
data = data.clip(lower=lower, upper=upper, axis=1)

scaler = StandardScaler()
data = pd.DataFrame(scaler.fit_transform(data), columns=reqcol)

X = data[['Unit_Cost']]
y = data['Revenue']

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=200)

model = LinearRegression()
model.fit(xtrain, ytrain)

print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")