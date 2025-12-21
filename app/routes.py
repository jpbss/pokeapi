from os import abort

from flask import Blueprint, render_template, url_for, redirect, request

from app.services import get_pokemon, get_all_pokemon_names

main = Blueprint('principal', __name__)

@main.route('/')
def home():
    lista_nomes = get_all_pokemon_names()
    return render_template("home.html", lista_nomes=lista_nomes)

@main.route('/search', methods=['POST'])
def search():
    pokemon = request.form['pokemon']
    return redirect(url_for('principal.index', pokemon=pokemon))

@main.route('/<string:pokemon>')
def index(pokemon):
    dados = get_pokemon(pokemon)

    if dados is None:
        abort(500)

    return render_template("index.html", dados=dados)

@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 404