import os
from flask import Flask
from .mots_caches import create_grid
from flask import render_template

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
    )

    @app.route('/')
    def index():
        grille, selection = create_grid()
        selection.sort()
        return render_template('grille.html', grid=grille, selection=selection)

    return app
