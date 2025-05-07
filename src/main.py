from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


class TitanicInput(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str


app = FastAPI()
model = joblib.load("titanic_model.pkl")


def preprocess_input(data: TitanicInput):
    df = pd.DataFrame([data.dict()])
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
    return df


@app.post("/predict")
def predict(data: TitanicInput):
    df = preprocess_input(data)
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
