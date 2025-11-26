import os
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df1 = get_csv(input())
    df2 = get_csv(input())

    df2.drop(columns=["DATE", "MONTH"], inplace=True)

    scaler = StandardScaler()
    scaled = pd.DataFrame(scaler.fit_transform(df1), columns=df1.columns)

    last_row = scaled.iloc[-1].to_frame().transpose()

    # the last row will be removed since -1 will be ignored in slice method
    scaled = scaled[:-1]
    corr_matrix = scaled.corr()
    corr_temp = corr_matrix["temperature"]

    features = corr_temp[abs(corr_temp) > 0.7].index.tolist()
    print(f"Features highly correlated with temperature (|corr| >=0.7): {features}")

    if "sunshine" in corr_temp.index:
        corr_temp = corr_temp.drop("sunshine")

    sorted_corr = corr_temp.sort_values(ascending=False).to_frame()
    print("Sorted correlation with temperature:")
    print(sorted_corr)


if __name__ == "__main__":
    compute()
