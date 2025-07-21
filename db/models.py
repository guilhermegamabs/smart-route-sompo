from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Ocorrencia(Base):
    __tablename__ = 'ocorrencias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(String)
    localidade = Column(String)
    ano = Column(Integer)
    ocorrencias = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
