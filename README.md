# Visualizador de Pokémon (PokeAPI)

Este é um projeto pessoal desenvolvido por um fã de Pokémon. Trata-se de uma aplicação web construída em **Python (Flask)** que consome a API pública [PokeAPI](https://pokeapi.co/) para listar, pesquisar e exibir detalhes sobre os Pokémon.

O diferencial deste projeto é o algoritmo de cálculo de fraquezas, que cruza os tipos do Pokémon para determinar os multiplicadores de dano reais.

## Funcionalidades

* **Catálogo Completo:** Carrega e lista os nomes de todos os Pokémon disponíveis na API.
* **Busca:** Permite pesquisar um Pokémon específico pelo nome.
* **Detalhes e Fraquezas:** Exibe os dados do Pokémon e calcula automaticamente as suas fraquezas acumuladas (ex: dano x2, x4) com base nos seus tipos e nas relações de dano (dano duplo, meio dano, imunidade).
* **Otimização:** Implementação de cache em memória para armazenar a lista de nomes e dados de tipos, reduzindo o número de requisições externas.

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Flask
* **Consumo de API:** Biblioteca `requests`
* **Front-end:** HTML/CSS (Templates Jinja2)

## Estrutura do Projeto

A lógica da aplicação está separada em camadas:

* **app/routes.py:** Gerencia as rotas web (`/`, `/search`, `/<pokemon>`) e renderiza os templates.
* **app/services.py:** Contém a regra de negócio. Responsável por buscar dados na PokeAPI e processar o cálculo de fraquezas.
* **app/templates:** Arquivos HTML da interface.
* **app/static:** Arquivos de estilo (CSS) e scripts (JS).

## Instalação e Execução

### Pré-requisitos
* Python 3 instalado.

### Passo a Passo

1.  Clone o repositório ou baixe os arquivos.
2.  Instale as dependências necessárias:
    ```bash
    pip install flask requests
    ```
3.  Execute a aplicação:
    ```bash
    python run.py
    ```
4.  Acesse no navegador: `http://localhost:5000`

## Lógica de Cálculo de Fraquezas

O sistema consulta as relações de dano de cada tipo do Pokémon (ex: Fogo, Voador) e multiplica os fatores:
* **Double Damage From:** Multiplicador x2.0
* **Half Damage From:** Multiplicador x0.5
* **No Damage From:** Multiplicador x0.0

No final, são exibidos apenas os tipos que resultam num multiplicador maior que 1.0 (fraquezas reais).

## Autoria

Projeto pessoal desenvolvido por João Pedro Balbino Santos Souza.
