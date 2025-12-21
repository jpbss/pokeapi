from flask import Blueprint, render_template, abort
from app.services import get_pokemon

main = Blueprint('principal', __name__)

@main.route('/<string:pokemon>')
def index(pokemon):
    dados = get_pokemon(pokemon)

    return render_template("index.html", dados=dados)