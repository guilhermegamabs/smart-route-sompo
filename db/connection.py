import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def get_engine():
    usuario = os.getenv('DB_USER')
    senha = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    porta = os.getenv('DB_PORT')
    banco = os.getenv('DB_NAME')

    URL = f'postgresql://{usuario}:{senha}@{host}:{porta}/{banco}'
    return create_engine(URL)

def create_tables(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
