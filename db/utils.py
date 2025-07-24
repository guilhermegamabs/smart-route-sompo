import pandas as pd
from db.models import Ocorrencia

def carregar_dados_do_banco(session):
    registros = session.query(Ocorrencia).all()

    lista = []
    for reg in registros:
        lista.append({
            'id': reg.id,
            'UF': reg.uf,
            'Localidade': reg.localidade,
            'Ano': reg.ano,
            'Ocorrências': reg.ocorrencias,
            'Latitude': reg.latitude,
            'Longitude': reg.longitude,
            'Risco': getattr(reg, 'risco', None)  # Caso queira puxar risco se já existir
        })

    return pd.DataFrame(lista)
