import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

file_name = input().strip()


df = pd.read_csv(os.path.join(sys.path[0], file_name))

for col in df.columns:
    df[col] = df[col].fillna(df[col].mean())

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
y = df_scaled["PremiumPrice"]

# Model 2: Two features 'Age', 'AnyTransplants'
X_2 = np.array(df_scaled[["Age", "AnyTransplants"]])
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(
    X_2, y, test_size=0.3, random_state=200
)
model_2 = LinearRegression().fit(X_train_2, y_train_2)
y_pred_2 = model_2.predict(X_test_2)

print("Model 2 (Age, AnyTransplants):")
print("Intercept:", model_2.intercept_)
print("Slopes:", model_2.coef_)
MSE_2 = mean_squared_error(y_test_2, y_pred_2)
MAE_2 = mean_absolute_error(y_test_2, y_pred_2)
RMSE_2 = MSE_2**0.5
print("MSE =", MSE_2)
print("RMSE =", RMSE_2)
print("MAE =", MAE_2)
print("R2 score =", r2_score(y_test_2, y_pred_2))


# Model 3a: Three features 'Age', 'AnyTransplants', 'NumberOfMajorSurgeries'
X_3a = df_scaled[["Age", "AnyTransplants", "NumberOfMajorSurgeries"]].values
X_train_3a, X_test_3a, y_train_3a, y_test_3a = train_test_split(
    X_3a, y, test_size=0.3, random_state=200
)
model_3a = LinearRegression().fit(X_train_3a, y_train_3a)
y_pred_3a = model_3a.predict(X_test_3a)

print("\nModel 3a (Age, AnyTransplants, NumberOfMajorSurgeries):")
print("Intercept:", model_3a.intercept_)
print("Slopes:", model_3a.coef_)
MSE_3a = mean_squared_error(y_test_3a, y_pred_3a)
MAE_3a = mean_absolute_error(y_test_3a, y_pred_3a)
RMSE_3a = MSE_3a**0.5
print("MSE =", MSE_3a)
print("RMSE =", RMSE_3a)
print("MAE =", MAE_3a)
print("R2 score =", r2_score(y_test_3a, y_pred_3a))

# Model 3b: Three features 'Age', 'AnyTransplants', 'AnyChronicDiseases'
X_3b = df_scaled[["Age", "AnyTransplants", "AnyChronicDiseases"]].values
X_train_3b, X_test_3b, y_train_3b, y_test_3b = train_test_split(
    X_3b, y, test_size=0.3, random_state=200
)
model_3b = LinearRegression().fit(X_train_3b, y_train_3b)
y_pred_3b = model_3b.predict(X_test_3b)

print("\nModel 3b (Age, AnyTransplants, AnyChronicDiseases):")
print("Intercept:", model_3b.intercept_)
print("Slopes:", model_3b.coef_)
MSE_3b = mean_squared_error(y_test_3b, y_pred_3b)
MAE_3b = mean_absolute_error(y_test_3b, y_pred_3b)
RMSE_3b = MSE_3b**0.5
print("MSE =", MSE_3b)
print("RMSE =", RMSE_3b)
print("MAE =", MAE_3b)
print("R2 score =", r2_score(y_test_3b, y_pred_3b))

# Model 4: Four features 'Age', 'AnyTransplants', 'AnyChronicDiseases', 'BloodPressureProblems'
X_4 = df_scaled[
    ["Age", "AnyTransplants", "AnyChronicDiseases", "BloodPressureProblems"]
].values
X_train_4, X_test_4, y_train_4, y_test_4 = train_test_split(
    X_4, y, test_size=0.3, random_state=200
)
model_4 = LinearRegression().fit(X_train_4, y_train_4)
y_pred_4 = model_4.predict(X_test_4)

print("\nModel 4 (Age, AnyTransplants, AnyChronicDiseases, BloodPressureProblems):")
print("Intercept:", model_4.intercept_)
print("Slopes:", model_4.coef_)
MSE_4 = mean_squared_error(y_test_4, y_pred_4)
MAE_4 = mean_absolute_error(y_test_4, y_pred_4)
RMSE_4 = MSE_4**0.5
print("MSE =", MSE_4)
print("RMSE =", RMSE_4)
print("MAE =", MAE_4)
print("R2 score =", r2_score(y_test_4, y_pred_4))
