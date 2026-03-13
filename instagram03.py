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

# Lista com os nomes dos campos
lista_campos = [
    "id",
    "caption",
    "media_type",
    "like_count",
    "comments_count",
    "media_url",
    "permalink"
]

# Segunda lista com os nomes dos campos
lista_campos_video = [
    "media_type",
    "like_count",
    "comments_count",
    "video_title",
    "thumbnail_url",
    "permalink",
    "views"
]


# Endpoint para listar todas as mídias do usuário
url = f"https://graph.instagram.com/me/media?fields={','.join(lista_campos)}&access_token={ACCESS_TOKEN}"

response = requests.get(url)
if response.status_code == 200:
    medias = response.json().get("data", [])
    for media in medias:
        print("ID:", media.get("id"))
        print("Legenda:", media.get("caption"))
        print("Tipo:", media.get("media_type"))
        print("Curtidas:", media.get("like_count"))
        print("Comentários:", media.get("comments_count"))
        print("Visualização de Reels: ", media.get("view_count"))
        # Para vídeos, buscar visualizações
        if media.get("media_type") == "VIDEO":
            video_url = f"https://graph.instagram.com/{media.get('id')}?fields={','.join(lista_campos_video)}&access_token={ACCESS_TOKEN}"
            print("URL do vídeo:", video_url)
            video_response = requests.get(video_url)
            print("Status Code:", video_response.status_code)
            if video_response.status_code == 200:
                video_data = video_response.json()
                print("Visualizações:", video_data.get("views"))

        print("-" * 40)
        print("\n")
else:
    print("Erro:", response.status_code, response.text)