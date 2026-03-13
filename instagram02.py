# Importa as bibliotecas necessárias
import json
import requests

from dotenv import load_dotenv
load_dotenv()
import os


# Substitua pelo seu token de acesso válido
ACCESS_TOKEN = os.getenv("API_META_ACCESS_TOKEN")

# Endpoint da API para obter informações do usuário autenticado
url = f"https://graph.instagram.com/me?fields=id,username&access_token={ACCESS_TOKEN}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("ID:", data.get("id"))
    print("Usuário:", data.get("username"))
else:
    print("Erro:", response.status_code, response.text)

# consultar dados API para obter as mídias do usuário


# Endpoint para listar todas as mídias do usuário
list_fields = "id,replies,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username,text,like_count,comments_count"
url = f"https://graph.instagram.com/me/media?fields={list_fields}&access_token={ACCESS_TOKEN}"

response = requests.get(url)

if response.status_code == 200:
    medias = response.json().get("data", [])
    save_path = "medias.json"
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(medias, f, ensure_ascii=False, indent=4)
else:
    print("Erro:", response.status_code, response.text)