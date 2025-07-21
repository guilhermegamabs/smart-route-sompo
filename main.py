import pandas as pd
from db.connection import get_engine, create_tables, get_session
from db.models import Ocorrencia

def importar_dados(session):
    df = pd.read_excel("data/base_unificada_ocorrencias_2015_2025.xlsx")

    for _, row in df.iterrows():
        ocorrencia = Ocorrencia(
            uf=row['UF'],
            localidade=row['Localidade'],
            ano=int(row['Ano']),
            ocorrencias=int(row['Ocorrências']),
            latitude=float(row['Latitude']),
            longitude=float(row['Longitude'])
        )
        session.add(ocorrencia)

    session.commit()
    print("Dados importados com sucesso!")

if __name__ == "__main__":
    engine = get_engine()
    create_tables(engine)
    session = get_session(engine)
    importar_dados(session)
