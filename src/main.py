# src/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model saat startup (1x saja)
model = joblib.load("models/titanic_model.pkl")

app = FastAPI(title="Titanic Survival Prediction API")

# Schema input menggunakan Pydantic
class Passenger(BaseModel):
    Pclass: int
    Sex: int          # 0 = female, 1 = male
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: int     # 0, 1, 2 (C, Q, S tergantung encoder)

@app.post("/predict")
def predict(passenger: Passenger):
    data = np.array([[ 
        passenger.Pclass, passenger.Sex, passenger.Age,
        passenger.SibSp, passenger.Parch, passenger.Fare, passenger.Embarked
    ]])

    prediction = model.predict(data)[0]
    return {"survived": int(prediction)}
