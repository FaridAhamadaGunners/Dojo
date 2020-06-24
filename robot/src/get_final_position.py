from typing import Union

def init_vars():
    """
    Initialisation des variables à 0

    :return: Renvoi les variables initialisées
    """
    x = 0
    y = 0
    pos_tete = 0
    return x,y,pos_tete


def load_dim(filepath: str) -> Union[int, int]:
    """
    Chargement des dimensions de l'espace depuis le fichier universe.txt

    :param filepath: String contenant le chemin d'accès au fichier universe.txt
    :return: Renvoi la valeur de width et de height
    """

    # Ouverture du fichier du fichier universe.txt
    file = open(filepath, "r")
    # Lecture de la première ligne et récupération de la valeur de width
    n = int(file.readline().split(":")[1].strip())
    # Lecture de la seconde ligne et récupération de la valeur de height
    p = int(file.readline().split(":")[1].strip())
    return n, p


def read_instruction(line: str) -> Union[str, int]:
    """
    Lecture ligne par ligne et parsing des instructions du fichier instruction_list.txt

    :param line: String contenant une ligne (ici du fichier instruction_list.txt)
    :return: La direction (right ou left) ainsi que le nombre de case de déplacement (1,2,...)
    """
    # Séparation de chacune des lignes du fichier par une virgule
    line = line.split(",")
    # Récupération de la direction qui constitue le premiere élément de ma liste. exemple : (right,3)
    direction = line[0].strip()
    # Récupération du nombre de déplacement sur le même principe que la direction
    case = int(line[1].strip())
    return direction, case


def position_tete(pos: int, x: int, y: int,
                  case: int, n: int, p: int, verbose: bool = False) -> Union[int, int]:
    """
    Référentiel des différentes actions à effectuer en fonction de la position de la tête du robot ainsi
    qu'en fonction de son déplacement dans l'espace dédié.

    :param pos: Int, définissant la position de la tête du robot. [0:'Haut';1:'Droite';2:'Bas';3:'Gauche']
    :param x: Int, position du robot sur l'axe des abcisse
    :param y: Int, position du robot sur l'axe des ordonnées
    :param case: Int, nombre de pas à effectuer par le robot
    :param n: Int, Largeur maximal de notre espace
    :param p: Int, Hauteur maximal de notre espace
    :param verbose: Boolean, initialisé à False mais à True permet d'afficher le parcours du robot
    :return: Renvoi la position du robot au couple (x,y) après une instruction effectuées
    """
    # Si la variable pos est égale à 0 c'est que la tête du robot est tourné vers le HAUT
    if pos == 0:
        # On incrémente y avec le nombre de pas à réaliser, cependant si cela excède la hauteur maximal de l'espace
        # on prend la valeur max - 1
        y = min(y+case, p-1)

    # Si la variable pos est égale à 1 c'est que la tête du robot est tourné vers la DROITE
    elif pos == 1:
        # On incrémente x avec le nombre de pas à réaliser, cependant si cela excède la largeur maximal de l'espace
        # on prend la valeur max - 1
        x = min(x+case, n-1)

    # Si la variable pos est égale à 2 c'est que la tête du robot est tourné vers la BAS
    elif pos == 2:
        # On décrémente y avec le nombre de pas à réaliser, cependant si cela excède la largeur minimal de l'espace
        # on prend le minimum donc 0
        y = max(y-case, 0)

    # Si la variable pos est égale à 3 c'est que la tête du robot est tourné vers la GAUCHE
    elif pos == 3:
        # On décrémente x avec le nombre de pas à réaliser, cependant si cela excède la hauteur minimal de l'espace
        # on prend le minimum donc 0
        x = max(x-case, 0)

    # De plus, en fonction de l'enchainement des instructions nous pouvons tomber sur des valeurs de "pos" non prise
    # en compte dans mon référentiel tel que [-1,-2,-3,-4,4,6 ...]
    # Les hardcoder aurait été une erreur et aurait overfit les instructions actuelles
    # La solution a été de calculer le reste de la division euclidienne de cette valeur non prise en charge dans mon
    # référentiel par 4 (pour mes 4 positions de la tête du robot) cela nous permet de rester dans un ensemble défini.
    # pos ∈ [0,3]
    elif pos < 0 or pos > 3:
        # La nouvelle valeur de pos après avoir calculé le modulo par 4
        new_pos = pos % 4
        # Appel récursive de la fonction position_tete avec la nouvelle valeur comprise dans l'ensemble [0,3]
        x, y = position_tete(new_pos, x, y, case, n, p)

    if verbose:
        print(x, y)

    return x, y


if __name__ == "__main__":
    # Chemin d'accès au fichier universe.txt
    universe_path = "Data/universe.txt"
    # Chemin d'accès au fichier instruction_list.txt
    instruction_path = "Data/instruction_list.txt"

    print("Chargement des dimensions ...")
    n, p = load_dim(universe_path)
    # Initialisation du robot à la position x et y (0,0) et la position de la tête à 0 : Haut
    x,y,pos_tete = init_vars()
    # Ouverture du fichier instruction_list.
    file = open(instruction_path, "r")

    print("Lecture des instructions ...")
    # On parcours chaque ligne de fichier et on éxècute chacune des instructions
    # afin d'avoir la position finale du robot
    for line in file:
        # Parsing des directions et nombre de pas à effectuer
        direction,case = read_instruction(line)
        # Si la direction est "right" on incrémentons de 1 la position de la tête
        # x et y prennent la valeur renvoyé par la fontion position_tete qui permet d'éxécuter les instructions
        if direction == "right":
            pos_tete = pos_tete + 1
            x,y = position_tete(pos_tete, x, y, case, n, p)
        # Tandis que lorsque la position "left" on décrémente de 1 la position de la tête
        # x et y prennent la valeur renvoyé par la fontion position_tete qui permet d'éxécuter les instructions
        else:
            pos_tete = pos_tete - 1
            x,y = position_tete(pos_tete, x, y, case, n, p)

    file.close()
    print(f"Le robot est arrivé à la position finale : {(x,y)}")
    




