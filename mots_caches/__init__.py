import os
from flask import Flask
from .mots_caches import create_grid

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
    )

    @app.route('/')
    def index():
        grille, selection = create_grid()
        html_grid = f"<pre>{'<br />'.join([' '.join(ligne) for ligne in grille])}</pre>"
        html_selection = f"<pre>{'<br />'.join(selection)}</pre>"
        return html_grid + "<br />" + html_selection

    return app
