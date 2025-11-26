import os
import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():

    # STEP 1 : Open the file and print first 5 rows
    df = get_csv(input())
    print("First 5 rows of dataset:")
    print(df.head())

    # STEP 2 : Print the availble columns
    print()
    print("Available Columns:")
    print(df.columns.to_list())

    # STEP 3 : Model Training
    print()

    x = np.array(df["global_radiation"])
    x = x.reshape(-1, 1)
    y = np.array(df["temperature"])

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=200
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    rscore = model.score(x_train, y_train)
    print("Model Trained")
    print(f"R² Score (Train): {rscore:.4f}")
    print(f"{'Intercept':<16}: {model.intercept_:.4f}")
    print(f"{'Slope':<16}: {model.coef_[0]:.4f}")

    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2Score = r2_score(y_test, y_pred)

    # STEP 4 : Evaluation Metrics

    print()
    print("Evaluation Metrics:")
    print(f"{'Mean Squared Error (MSE)':<25}: {mse:.4f}")
    print(f"{'Mean Absolute Error (MAE)':<25}: {mae:.4f}")
    print(f"{'Root Mean Squared Error':<25}: {rmse:.4f}")
    print(f"{'R² Score (Test)':<25}: {r2Score:.4f}")


if __name__ == "__main__":
    compute()
