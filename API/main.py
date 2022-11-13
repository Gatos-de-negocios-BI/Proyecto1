# Correr los siguientes comandos:
#   pip install "uvicorn[standard]"
#   pip install fastapi
#   pip install pydantic

# Para correr el servidor:
#   uvicorn main:app --reload

from typing import List

import pandas as pd
from fastapi import FastAPI

from DataModel import DataModel
from prediction_model import PredictionModel

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global prediction_model
    prediction_model = PredictionModel()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def make_prediction(dataModel: List[DataModel]):
    df = pd.DataFrame([x.dict() for x in dataModel])
    df.columns = dataModel[0].columns()
    results = prediction_model.make_prediction(df)
    return results.tolist()
