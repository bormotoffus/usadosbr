import pandas as pd
from sqlalchemy import create_engine

caminho_arquivo_csv = 'caminho/do/seu/arquivo.csv'
df_csv = pd.read_csv(caminho_arquivo_csv)
print(df_csv.head())

host = 'mysql-04-prd.cluster-czeqw00r0041.sa-east-1.rds.amazonaws.com'
port = '3306'
database = 'ubr_db'
usuario = 'powerbi'
senha = '111111'

connection_str = f"mysql+pymysql://{usuario}:{senha}@{host}:{port}/{database}"
engine = create_engine(connection_str)

with engine.connect() as conn:
    for index, row in df_csv.iterrows():
        id_registro = row['id'] 
        novo_company_type = row['Novo company_type']
        query_update = f"UPDATE advertisers SET company_type = '{novo_company_type}' WHERE id = {id_registro};"
        conn.execute(query_update)
