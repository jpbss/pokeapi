# ⚡ PokéDex Web App

![Badge Status](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

> *"Gotta Catch 'Em All!"*

Este é um projeto pessoal desenvolvido pela simples paixão por **Pokémon** e tecnologia. O objetivo foi criar uma Pokédex interativa que não fosse apenas uma lista de dados, mas que trouxesse uma experiência visual rica e funcionalidades úteis para treinadores, como o cálculo real de fraquezas.

A aplicação consome a [PokeAPI](https://pokeapi.co/) e foi construída utilizando **Python (Flask)** no back-end e **CSS** no front-end.

## 🎨 Destaques de Design & UX

Como um projeto feito de fã para fã, a interface recebeu atenção especial para ser fiel à identidade visual da franquia:

### 1. Identidade Visual Dinâmica
As cores da interface adaptam-se automaticamente ao tipo do Pokémon. Foram criadas classes CSS específicas para cada um dos 18 tipos elementais (ex: `.type-fire`, `.type-water`), garantindo a imersão.

### 2. Modo Shiny ✨
Implementação de um botão especial que permite alternar instantaneamente a visualização do Pokémon para a sua versão **Shiny**, carregando os sprites correspondentes.

### 3. Visualização de Stats
Os atributos de batalha (HP, Ataque, Defesa, etc.) são exibidos através de **barras de progresso coloridas**, facilitando a leitura rápida do potencial do Pokémon.

### 4. Busca Inteligente
O sistema conta com um autocomplete customizado que exibe sugestões com **miniaturas** dos Pokémon enquanto digita.
---

## 🧠 Lógica e Back-end

O diferencial técnico deste projeto está no processamento de dados no servidor:

* **Calculadora de Fraquezas Reais:** Diferente de muitas Pokédex que mostram apenas os tipos, este sistema cruza os dados de defesa (dano x2, x0.5, x0) de *todos* os tipos do Pokémon.
    * *Exemplo:* Um Charizard (Fogo/Voador) recebe dano x4 de Pedra. O algoritmo em Python calcula isso automaticamente e exibe apenas o multiplicador final.
* **Otimização com Cache:** Para garantir performance e respeitar os limites da API pública, a lista de todos os Pokémon e os dados de tipos são cacheados em memória na primeira execução.
* **Tratamento de Erros:** Páginas personalizadas para erros 404 (Pokémon não encontrado) e 500 (Erro de API).

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Passo a Passo

1.  Clone este repositório.
2.  Instale as dependências:
    ```bash
    pip install flask requests
    ```
3.  Execute a aplicação:
    ```bash
    python run.py
    ```
4.  Abra no seu navegador: `http://localhost:5000`

## 📸 Screenshots

| Página Inicial (Busca) | Detalhes do Pokémon |
|:---:|:---:|
| <img width="1481" height="928" alt="image" src="https://github.com/user-attachments/assets/928a396b-c567-49a6-87c1-d0cdd4af57fd" />
| <img width="1481" height="928" alt="image" src="https://github.com/user-attachments/assets/0615aa93-7bf8-44f5-8fe2-ce60d5a8a67c" />
|

## 🛠 Tecnologias Utilizadas

* **Back-end:** Python, Flask, Requests.
* **Front-end:** HTML5, CSS3 (Grid & Flexbox), JavaScript.
* **Dados:** [PokeAPI v2](https://pokeapi.co/).

## ✒️ Autoria

Desenvolvido com ❤️ e ☕ por **João Pedro Balbino Santos Souza**.
