import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from joblib import load
import numpy as np

DATA_FOLDER = "../Data"


def delete_whitespace(string: str) -> str:
    # Replace whitespace by underscore
    return string.replace(" ", "_")


def label_or_Dummies(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    # Case we want to predict just one observation
    if df.shape[0] < 5:
        return pd.get_dummies(data=df, columns=cols)
    else:
        le = LabelEncoder()
        cols_to_dummies = []
        for col in cols:
            if df[col].nunique() > 2:
                cols_to_dummies.append(col)
            else:
                df[col] = le.fit_transform(df[col])
    return pd.get_dummies(data=df, columns=cols_to_dummies)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    new_cols = []
    # Rename columns
    for i in range(len(df.columns)):
        new_cols.append(delete_whitespace(df.columns[i]))
    df.columns = new_cols

    # Dummies variables and labelencoder
    cols = df.columns
    df = label_or_Dummies(df, cols)

    return df


def load_training_data():
    df = pd.read_csv(os.path.join(DATA_FOLDER, "Transformed Data Set - Sheet1.csv"))
    df = preprocess(df)
    X = df.drop(['Gender'], axis=1)
    y = df.Gender.copy()

    return X, y


def gender_predict(X: pd.Series, y: pd.Series):
    clf = load('../Model/lr.joblib')
    clf.fit(X, y)
    return clf.predict(X)

