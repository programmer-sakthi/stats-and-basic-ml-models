import os
import sys
import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    # Receive the file
    df = get_csv(input())

    # Required columns
    reqcol = ["global_radiation", "humidity", "pressure", "temperature"]

    # Fill missing values
    df[reqcol] = df[reqcol].fillna(df[reqcol].mean())

    # Feature / target split
    x = df[["global_radiation", "humidity", "pressure"]]
    y = df["temperature"]

    # Train/test split
    xtrain, xtest, ytrain, ytest = train_test_split(
        x, y, test_size=0.30, random_state=200
    )

    # Train model
    model = LinearRegression()
    model.fit(xtrain, ytrain)

    # Prediction
    ypred = model.predict(xtest)

    # Metrics
    mse = mean_squared_error(ytest, ypred)
    mae = mean_absolute_error(ytest, ypred)
    rmse = math.sqrt(mse)
    r2 = r2_score(ytest, ypred)

    # Results
    print("Multiple Linear Regression (3 features) Results")
    print(f"Intercept: {model.intercept_:.4f}")
    print("Slopes (coefficients):")
    print(f" global_radiation: {model.coef_[0]:.4f}")
    print(f" humidity: {model.coef_[1]:.4f}")
    print(f" pressure: {model.coef_[2]:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R2 Score: {r2:.4f}")


if __name__ == "__main__":
    compute()
