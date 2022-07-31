from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class iris(BaseModel):
    a: float
    b: float
    c: float
    d: float

from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

# we are loading the model using pickle
model = pickle.load(open('model_iris', 'rb'))

@app.post('/make_predictions')
async def make_predictions(features: iris):
    return ({"prediction": str(model.predict([[features.a, features.b, features.c, features.d]])[0])})