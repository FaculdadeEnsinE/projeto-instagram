# Importa as bibliotecas necessárias
import json

# pandas para manipulação de dados
import pandas as pd

# Glob para ler os arquivos JSON
import glob

# converter o json para duckdb
import duckdb

conn = duckdb.connect(database='./duckdb/instagram.duckdb', read_only=False)
conn.execute("DROP TABLE IF EXISTS medias")

# Criar tabela se não existir
conn.execute("""
    CREATE TABLE IF NOT EXISTS medias (
        id BIGINT,                -- ID da mídia
        caption TEXT,             -- Legenda
        media_type TEXT,          -- Tipo (IMAGE, VIDEO, CAROUSEL_ALBUM)
        like_count INTEGER,       -- Número de curtidas
        comments_count INTEGER,   -- Número de comentários
        media_url TEXT,           -- URL da mídia
        permalink TEXT,           -- Link permanente
        timestamp TIMESTAMP,      -- Data/hora da publicação
        username TEXT             -- Nome de usuário
    )
""")


# Listar os arquivos JSON na pasta
json_files = glob.glob("./json/*.json")

for file in json_files:
    print(f"Abrindo arquivo: {file}")
    with open(file, "r", encoding="utf-8") as f:
        #convertendo o JSON para um DataFrame do pandas
        df = pd.json_normalize(json.load(f))

        # ou para inserir dados adicionais:
        conn.execute("INSERT INTO medias \
                     SELECT id,caption, media_type, like_count, comments_count, media_url, permalink, timestamp,username \
                     FROM df")

# close the connection
conn.close()