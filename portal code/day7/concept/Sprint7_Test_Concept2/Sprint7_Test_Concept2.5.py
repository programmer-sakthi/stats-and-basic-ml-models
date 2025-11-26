import pandas as pd
import os
import sys
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

reqcol = ["global_radiation", "humidity", "temperature"]

df[reqcol] = df[reqcol].fillna(df[reqcol].mean())

x = df[["global_radiation", "humidity"]]
y = df["temperature"]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=200)

model = LinearRegression()
model.fit(xtrain, ytrain)

ypred = model.predict(xtest)

mse = mean_squared_error(ytest, ypred)
rmse = math.sqrt(mse)
mae = mean_absolute_error(ytest, ypred)
r2 = r2_score(ytest, ypred)

print("Multiple Linear Regression Model Results")
print(f"Intercept: {model.intercept_:.4f}")
print(
    f"Slopes (coefficients): global_radiation = {model.coef_[0]:.4f}, humidity = {model.coef_[1]:.4f}"
)
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R2 Score: {r2:.4f}")
