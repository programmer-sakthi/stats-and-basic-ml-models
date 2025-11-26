import pandas as pd
import os
import sys
import math
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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
df = df.fillna(df.mean())
print()


for col in df.columns:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper, axis=0)

print("Outlier treatment (IQR Winsorization) done.")
print()

scaler = StandardScaler()
scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("First 5 Rows after Scaling:")
print(scaled.head())
print()

x = scaled[["Age"]]
y = scaled["PremiumPrice"]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=200)
model = LinearRegression()
model.fit(xtrain, ytrain)
ypred = model.predict(xtest)

mse = mean_squared_error(ytest, ypred)
rmse = math.sqrt(mse)
mae = mean_absolute_error(ytest, ypred)
r2 = r2_score(ytest, ypred)

print("Model 1 (Age):")
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
print("MSE = ", mse)
print("RMSE = ", rmse)
print("MAE = ", mae)
print("R2 score = ", r2)
