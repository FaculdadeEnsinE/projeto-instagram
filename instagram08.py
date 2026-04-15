# Importa as bibliotecas necessárias
import json

# pandas para manipulação de dados
import pandas as pd

# Glob para ler os arquivos JSON
import glob

# converter o json para duckdb
import duckdb

conn = duckdb.connect(database='./duckdb/instagram.duckdb', read_only=False)
conn.execute("DROP TABLE IF EXISTS bronze_post")
conn.execute("DROP TABLE IF EXISTS silver_post")
conn.execute("DROP TABLE IF EXISTS gold_post")
# close the connection
conn.close()

# Criar tabela se não existir
conn.execute("""
    CREATE TABLE bronze_post as
    SELECT * FROM medias
""")

conn.execute("""
    CREATE TABLE silver_post as
    SELECT * FROM bronze_post
""")

list_fala = ['faala','faaala','faaala','faaaala','faaaaala','faaaaaala']

for text_fala in list_fala:
    conn.execute(f"""
        UPDATE silver_post
        SET caption = REPLACE(caption, '{text_fala}', 'Fala')
        WHERE caption LIKE '%{text_fala}%'
    """)

conn.execute("""
    UPDATE silver_post
    SET caption = REPLACE(UPPER(caption), 'FALA FORROZEIROS DO MEU CORAÇÃO', 'Fala Forrozeiros do meu coração')
    WHERE UPPER(caption) LIKE '%FALA FORROZEIROS DO MEU CORAÇÃO%'
""")


# close the connection
conn.close()