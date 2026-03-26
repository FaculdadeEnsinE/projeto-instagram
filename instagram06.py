# Importa as bibliotecas necessárias
import json
import requests

from dotenv import load_dotenv
load_dotenv()
import os


# Substitua pelo seu token de acesso válido
ACCESS_TOKEN = os.getenv("API_META_ACCESS_TOKEN")

# Endpoint da API para obter informações do usuário autenticado
url = f"https://graph.instagram.com/me?\
fields=id,username,account_type,media_count,name,biography,profile_picture_url,followers_count,follows_count\
&access_token={ACCESS_TOKEN}"
# id	O ID numérico da conta Instagram Business.
# ig_id	O ID legado do Instagram (útil para algumas integrações antigas).
# username	O @ do perfil.
# name	Nome de exibição do perfil.
# biography	O texto da bio.
# profile_picture_url	URL da foto de perfil.
# followers_count	Quantidade total de seguidores.
# follows_count	Quantidade de perfis que a conta segue.
# media_count	Total de publicações.

# tasks, instagram_business_account\
#id, caption, media_type, media_url, permalink, timestamp, thumbnail_url

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    # print("ID:", data.get("id"))
    # print("Usuário:", data.get("username"))
    # print("Tipo de Conta:", data.get("account_type"))
    # print("Quantidade de Mídias:", data.get("media_count"))
    # print("Dados completos:", json.dumps(data, indent=4))
else:
    print("Erro:", response.status_code, response.text)
exit()
# consultar dados API para obter as mídias do usuário

# Lista com os nomes dos campos
lista_campos = [
    "id",
    "caption",
    "media_type",
    "like_count",
    "comments_count",
    "media_url",
    "permalink",
    "timestamp",
    "thumbnail_url",
    "username",
    "children{media_url}"
]

lista_media_type = ["IMAGE", "VIDEO", "CAROUSEL_ALBUM"]

endpoint = "https://graph.instagram.com/me/media"

# Endpoint para listar todas as mídias do usuário
url = f"{endpoint}?fields={','.join(lista_campos)}&access_token={ACCESS_TOKEN}"

print("URL:", url)
response = requests.get(url)
if response.status_code == 200:
    i = 1
    medias = response.json().get("data", [])
    next = response.json().get("paging", {}).get("next", None)
    # Salvando em arquivo JSON
    with open(f"./json/media_{i}.json", "w", encoding="utf-8") as f:
        print(f'{i}o. salvamento')
        json.dump(medias, f, ensure_ascii=False, indent=4)

    # Pegar o próximo link para obter as próximas mídias
    while True:
        if not next:
            print("Não existe próxima página.")
            break
        response = requests.get(next)
        if response.status_code == 200:
            i += 1
            medias = response.json().get("data", [])
            next = response.json().get("paging", {}).get("next", None)
            with open(f"./json/media_{i}.json", "w", encoding="utf-8") as f:
                print(f'{i}a. salvamento')
                json.dump(medias, f, ensure_ascii=False, indent=4)
        else:
            print("Erro ao obter próxima página:", response.status_code, response.text)
            break

else:
    print("Erro:", response.status_code, response.text)
