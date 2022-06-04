import random
from typing import List

from flask import Flask
app = Flask(__name__)

def cache_mot(grille : List[List[str]], mot: str) -> bool:
    for essai in range(3):
        try:
            direction = random.randint(0, 2)
            if direction == 0:
                # horizontal
                x = random.randint(0, len(grille[0]) - len(mot))
                y = random.randint(0, len(grille) - 1)
                for xi in range(0, len(mot)):
                    if grille[y][x + xi] not in ("-", mot[xi]):
                        raise Exception("collision")
                for xi in range(0, len(mot)):
                    grille[y][x+xi] = mot[xi]
            elif direction == 1:
                # vertical
                x = random.randint(0, len(grille[0]) - 1)
                y = random.randint(0, len(grille) - len(mot))
                for yi in range(0, len(mot)):
                    if grille[y + yi][x] not in ("-", mot[yi]):
                        raise Exception("collision")
                for yi in range(0, len(mot)):
                    grille[y+yi][x] = mot[yi]
            else:
                # diagonal
                x = random.randint(0, len(grille[0]) - len(mot))
                y = random.randint(0, len(grille) - len(mot))
                for yi in range(0, len(mot)):
                    if grille[y + yi][x + yi] not in ("-", mot[yi]):
                        raise Exception("collision")
                for yi in range(0, len(mot)):
                    grille[y+yi][x+yi] = mot[yi]
            return True
        except Exception:
            continue
    return False

def fill_grid_with_letters(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == "-":
                grille[i][j] = random.choice("abcdefghijklmnopqrstuvwxyz")

def create_grid():
    # Utilise une liste de mots
    with open("mots.txt", "r") as f:
        mots = f.read().splitlines()
    grille = [
        ["-" for _ in range(0, 10)]
        for _ in range(0, 10)
    ]
    nb_mots = int(len(grille) * 1.5)
    selection = []
    while nb_mots > 0:
        mot = random.choice(mots)
        if mot in selection:
            continue
        if cache_mot(grille, mot):
            nb_mots -= 1
            selection.append(mot)
    fill_grid_with_letters(grille)
    return grille, selection

@app.route('/')
def index():
    grille, selection = create_grid()
    html_grid = f"<pre>{'<br />'.join([' '.join(ligne) for ligne in grille])}</pre>"
    html_selection = f"<pre>{'<br />'.join(selection)}</pre>"
    return html_grid + "<br />" + html_selection
   
if __name__ == "__main__":
    app.run()
