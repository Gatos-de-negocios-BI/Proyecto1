from sqlalchemy import String, Integer, DateTime
from sqlalchemy.sql.schema import Column
from database import Base
import datetime

class Publicacion(Base):
    __tablename__ = "publicacion"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    date = Column(DateTime)
    classification = Column(String)
    person = Column(String)
