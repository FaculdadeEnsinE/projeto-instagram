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
    "permalink",
    "timestamp"

]

endpoint = "https://graph.instagram.com/me/media"

# Endpoint para listar todas as mídias do usuário
url = f"{endpoint}?fields={','.join(lista_campos)}&access_token={ACCESS_TOKEN}"
print("URL:", url)
response = requests.get(url)
if response.status_code == 200:
    medias = response.json()
    next = response.json().get("paging", {}).get("next", None)
    # Salvando em arquivo JSON
    with open("medias.json", "w", encoding="utf-8") as f:
        i = 1
        print(f'{i}o. salvamento')
        json.dump(medias, f, ensure_ascii=False, indent=4)

    # Pegar o próximo link para obter as próximas mídias
    while True:
        if not next:
            print("Não existe próxima página.")
            break
        response = requests.get(next)
        if response.status_code == 200:
            medias = response.json()
            next = response.json().get("paging", {}).get("next", None)
            with open("medias.json", "a", encoding="utf-8") as f:
                i += 1
                print(f'{i}a. salvamento')
                json.dump(medias, f, ensure_ascii=False, indent=4)
        else:
            print("Erro ao obter próxima página:", response.status_code, response.text)
            break

else:
    print("Erro:", response.status_code, response.text)
