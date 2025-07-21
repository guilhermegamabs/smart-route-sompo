import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from db.connection import get_engine, create_tables, get_session
from db.models import Ocorrencia

def importar_dados(session, df):
    registros_inseridos = 0

    for _, row in df.iterrows():
        # Verifica se o registro já existe no banco
        existe = session.query(Ocorrencia).filter_by(
            uf=row['UF'],
            localidade=row['Localidade'],
            ano=int(row['Ano'])
        ).first()

        if existe:
            continue  # Pula duplicados

        # Cria novo objeto Ocorrencia
        ocorrencia = Ocorrencia(
            uf=row['UF'],
            localidade=row['Localidade'],
            ano=int(row['Ano']),
            ocorrencias=int(row['Ocorrências']),
            latitude=float(row['Latitude']),
            longitude=float(row['Longitude'])
        )

        session.add(ocorrencia)
        registros_inseridos += 1

    session.commit()
    print(f"✅ {registros_inseridos} novos registros inseridos no banco.")

def main():
    try:
        print("🔌 Conectando ao banco...")
        engine = get_engine()
        create_tables(engine)
        session = get_session(engine)
        print("✅ Conexão bem-sucedida!")

        # Carrega os dados do Excel
        df = pd.read_excel("data/base_unificada_ocorrencias_2015_2025.xlsx")

        print(f"📊 Total de registros na planilha: {len(df)}")
        importar_dados(session, df)

    except SQLAlchemyError as e:
        print(f"❌ Erro no banco de dados: {e}")
    except FileNotFoundError:
        print("❌ Arquivo Excel não encontrado. Verifique o caminho.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    finally:
        session.close()
        print("🔒 Sessão finalizada.")

if __name__ == "__main__":
    main()
