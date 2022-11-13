from pydantic import BaseModel

class CreatePublicacion(BaseModel):
    text: str
    person: str

