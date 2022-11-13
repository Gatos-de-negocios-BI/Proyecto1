from pydantic import BaseModel
from datetime import datetime

class DataModel(BaseModel):
# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    text: str

#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["text"]

class Publicacion(BaseModel):
    id: int
    text: str
    date: datetime
    classification: str
    person: str

    class Config:
        orm_mode = True
