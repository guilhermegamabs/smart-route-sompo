def classificar_niveis_risco(df):
    # Agrupa por UF e calcula a média por UF
    medias_por_uf = df.groupby('UF')['Ocorrências'].mean().to_dict()

    def classificar(row):
        media_uf = medias_por_uf.get(row['UF'], 1)
        if row['Ocorrências'] >= media_uf * 1.5:
            return 'Alto'
        elif row['Ocorrências'] >= media_uf * 0.7:
            return 'Médio'
        else:
            return 'Baixo'

    df['Risco'] = df.apply(classificar, axis=1)
    return df
