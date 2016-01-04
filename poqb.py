from Cube import Cube
from utils import Array, colorize, translate_mvt, readArgs
from algo import algo_cfop
from lire_entree import lecture_cube
from tuto import tuto

DEFAULT_CUBE = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'

def solve(cube_c54):
    """La fonction principale du projet qui résoud un Rubik's Cube.

    :param cube_c54: passé sous sa forme '54 facettes colorées'
           O G R
           B W Y
           B G B
    G Y Y  O Y O  W O W  G R Y
    O O O  B G B  R R Y  R B W
    W W R  B W Y  G R O  W G R
           Y B R
           G Y W
           B O G
    :return: une chaîne de caractères qui encode la manoeuvre
    qui mène du cube de départ à la permutation monochrome.

    :Example:

    solve('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG')

    """
    err, c = lecture_cube(cube_c54)
    if err:
        return err, None
    else:
        return None, algo_cfop(c), c

if __name__=="__main__":
    """
    :Example:
        python poqb.py
        python poqb.py -c YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW
        python poqb.py --cube=YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW
    """

    #On récupère le cube en paramètre ou on utilise celui par défaut
    params = readArgs()
    cube = str(params['cube']) if 'cube' in params else DEFAULT_CUBE

    err, resolution, c = solve(cube)
    if err:
        print("Erreur dans la lecture du cube : " + err)
    elif 'tuto' in params:
        print('Résolution de :', "".join([colorize(x) for x in cube]))
        tuto(c, resolution)
    else:
        print('Résolution de :', "".join([colorize(x) for x in cube]))
        resolution = " ".join([translate_mvt(x) for x in resolution])
        print("Exécuter la manoeuvre {}".format(resolution))
        

