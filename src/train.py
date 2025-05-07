import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from preprocess import preprocess


def train():
    df = pd.read_csv("data/train.csv")
    df = preprocess(df)
    X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
    y = df["Survived"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    joblib.dump(model, "titanic_model.pkl")


if __name__ == "__main__":
    train()
