import random
from typing import List

def cache_mot(grille : List[List[str]], mot: str) -> bool:
    for essai in range(10):
        try:
            direction = random.randint(0, 9)
            if direction == 0:
                # horizontal
                x = random.randint(0, len(grille[0]) - len(mot))
                y = random.randint(0, len(grille) - 1)
                for xi in range(0, len(mot)):
                    if grille[y][x + xi] not in ("-", mot[xi]):
                        raise Exception("collision")
                for xi in range(0, len(mot)):
                    grille[y][x+xi] = mot[xi]
            elif direction in (1,2,3) :
                # vertical
                x = random.randint(0, len(grille[0]) - 1)
                y = random.randint(0, len(grille) - len(mot))
                for yi in range(0, len(mot)):
                    if grille[y + yi][x] not in ("-", mot[yi]):
                        raise Exception("collision")
                for yi in range(0, len(mot)):
                    grille[y+yi][x] = mot[yi]
            elif direction in (4,5,6):
                # diagonale bas droite
                x = random.randint(0, len(grille[0]) - len(mot))
                y = random.randint(0, len(grille) - len(mot))
                for yi in range(0, len(mot)):
                    if grille[y + yi][x + yi] not in ("-", mot[yi]):
                        raise Exception("collision")
                for yi in range(0, len(mot)):
                    grille[y+yi][x+yi] = mot[yi]
            else:
                # diagonale bas gauche
                x = random.randint(0, len(grille[0]) - len(mot))
                y = random.randint(len(mot) - 1, len(grille))
                for yi in range(0, len(mot)):
                    if grille[y - yi][x + yi] not in ("-", mot[yi]):
                        raise Exception("collision")
                for yi in range(0, len(mot)):
                    grille[y-yi][x+yi] = mot[yi]
            return True
        except Exception:
            continue
    return False

def fill_grid_with_letters(grille):
    letters_in_grid = []
    for line in grille:
        for letter in line:
            if letter != "-":
                letters_in_grid.append(letter)
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == "-":
                grille[i][j] = random.choice(letters_in_grid)

def create_grid():
    # Utilise une liste de mots
    with open("mots.txt", "r") as f:
        mots = f.read().splitlines()
    grille = [
        ["-" for _ in range(0, 15)]
        for _ in range(0, 15)
    ]
    nb_mots = int(len(grille) * 1.5)
    selection = []
    while nb_mots > 0 and len(mots) > 0:
        mot = random.choice(mots)
        if cache_mot(grille, mot):
            nb_mots -= 1
            selection.append(mot)
        mots.remove(mot)
    fill_grid_with_letters(grille)
    return grille, selection
