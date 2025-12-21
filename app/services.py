import requests
from config import Config

type_data_cache = {}

def get_type_data(type_name):
    if type_name in type_data_cache:
        return type_data_cache[type_name]

    url = f"https://pokeapi.co/api/v2/type/{type_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        type_data_cache[type_name] = data
        return data
    return None


def calculate_weaknesses(types_list):
    """
    Calcula as fraquezas acumuladas com base nos tipos do Pokémon.
    Retorna um dicionário: {'rock': 4.0, 'water': 2.0, ...}
    """
    multipliers = {}

    for t_info in types_list:
        t_name = t_info['type']['name']
        t_data = get_type_data(t_name)

        if not t_data:
            continue

        relations = t_data['damage_relations']

        for t in relations['double_damage_from']:
            name = t['name']
            multipliers[name] = multipliers.get(name, 1.0) * 2.0

        for t in relations['half_damage_from']:
            name = t['name']
            multipliers[name] = multipliers.get(name, 1.0) * 0.5

        for t in relations['no_damage_from']:
            name = t['name']
            multipliers[name] = multipliers.get(name, 1.0) * 0.0

    # Filtra apenas o que é fraqueza (> 1.0)
    # Ex: { 'rock': 4.0, 'water': 2.0 }
    weaknesses = {k: v for k, v in multipliers.items() if v > 1.0}
    return weaknesses


lista_pokemons_cache = []


def get_all_pokemon_names():
    global lista_pokemons_cache
    if lista_pokemons_cache:
        return lista_pokemons_cache

    url = Config.API_URL_BASE + "?limit=10000"
    try:
        response = requests.get(url)
        data = response.json()
        lista_pokemons_cache = []
        for p in data['results']:
            pid = p['url'].split('/')[-2]
            lista_pokemons_cache.append({'name': p['name'], 'id': pid})
        return lista_pokemons_cache
    except requests.exceptions.RequestException:
        return []


def get_pokemon(pokemon):
    url = Config.API_URL_BASE + pokemon.lower()
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return None

        dados = response.json()

        dados['weaknesses'] = calculate_weaknesses(dados['types'])

        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return None