# Correr los siguientes comandos:
#   pip install "uvicorn[standard]"
#   pip install fastapi
#   pip install pydantic

# Para correr el servidor:
#   uvicorn main:app --reload

from typing import List

import pandas as pd
from database import get_db
import DataModel
from fastapi import Depends, FastAPI
from models import Publicacion
from prediction_model import PredictionModel
from schemas import CreatePublicacion
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_event():
    global prediction_model
    prediction_model = PredictionModel()

@app.get("/")
def read_root():
    return {"Hello": "World ඞ"}


@app.post("/predict")
def make_prediction(dataModel: List[DataModel.DataModel]):
    df = pd.DataFrame([x.dict() for x in dataModel])
    df.columns = dataModel[0].columns()
    results = prediction_model.make_prediction(df)
    return results.tolist()

@app.post("/")
def create_publicacion(publicacion: CreatePublicacion, db: Session = Depends(get_db)):
    classificationgot = prediction_model.make_prediction(pd.DataFrame([publicacion.text], columns=["text"]))
    dateActual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if classificationgot[0] == 1:
        classificationgot = "suicide"
    else:
        classificationgot = "non-suicide"

    to_create = Publicacion(
        id=4000000,
        text=publicacion.text,
        date=dateActual,
        classification=classificationgot,
        person=publicacion.person
    )
    db.add(to_create)
    db.commit()
    return {}

@app.get("/publis", response_model=List[DataModel.Publicacion])
def show_publis(db: Session = Depends(get_db)):
    publis = db.query(Publicacion).all()
    return publis

@app.get("/lastpublic", response_model = List[DataModel.Publicacion])
def show_last_public(db: Session = Depends(get_db)):
    publics = db.query(Publicacion).filter(Publicacion.id < 60).all()
    return publics
