# src/train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from preprocess import preprocess_data

def main():
    # Load data
    df = pd.read_csv("data/train.csv")

    # Preprocess
    X, y = preprocess_data(df)

    # Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Simpan model
    joblib.dump(model, "models/titanic_model.pkl")
    print("Model trained and saved to models/titanic_model.pkl")

if __name__ == "__main__":
    main()
