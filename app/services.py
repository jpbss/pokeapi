import requests
from config import Config

def get_pokemon(pokemon):
    url = Config.API_URL_BASE + pokemon
    response = requests.get(url)

    try:
        dados = response.json()
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return e