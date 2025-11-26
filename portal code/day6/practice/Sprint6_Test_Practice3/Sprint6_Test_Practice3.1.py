import pandas as pd
import os
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import math

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

req = ["Customer_Age", "Order_Quantity", "Unit_Cost", "Unit_Price", "Revenue"]
# df = df.fillna(df.mean(numeric_only=True))
data = df[req].copy()

data = data.astype("float")

data.fillna(data.mean(), inplace=True)

Q1, Q3 = data.quantile(0.25), data.quantile(0.75)
IQR = Q3 - Q1
data = data.clip(Q1 - 1.5 * IQR, Q3 + 1.5 * IQR, axis=1)

scaler = StandardScaler()
scaled = pd.DataFrame(scaler.fit_transform(data), columns=req)

x = scaled[["Unit_Cost"]]
y = scaled["Revenue"]

Xtrain, Xtest, Ytrain, Ytest = train_test_split(x, y, test_size=0.3, random_state=200)

model = LinearRegression()
model.fit(Xtrain, Ytrain)

y_pred = model.predict(Xtest)

mse = mean_squared_error(Ytest, y_pred)
mae = mean_absolute_error(Ytest, y_pred)
rmse = math.sqrt(mse)
r2 = r2_score(Ytest, y_pred)

print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R2 Score: {r2:.4f}")
