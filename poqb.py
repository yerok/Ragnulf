from Cube import Cube
from utils import Array, colorize, translate_mvt, readArgs
from algo import algo_cfop
from lire_entree import lecture_cube
from tuto import tuto

DEFAULT_CUBE = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'

def solve(cube_c54):
    """
    solve

    La fonction principale du projet qui résoud un Rubik's Cube.

    :Args:
        cube_c54    {String}     Le cube passé sous sa forme '54 facettes colorées'
                                           O G R
                                           B W Y
                                           B G B
                                    G Y Y  O Y O  W O W  G R Y
                                    O O O  B G B  R R Y  R B W
                                    W W R  B W Y  G R O  W G R
                                           Y B R
                                           G Y W
                                           B O G

    :Returns:
        {String}    une chaîne de caractères qui encode la manoeuvre
                    qui mène du cube de départ à la permutation monochrome.

    :Example:
        solve('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG')

    """
    err, mvts, _ = solve_full(cube_c54)
    print(err)
    if err:
        return err
    else:
        mvts = [translate_mvt(m) for m in mvts] #on remplace les i en '
        return ''.join(mvts)

def solve_full(cube_c54):
    """
    solve_full

    :Args:
        cube_c54    {String}     Le cube passé sous sa forme '54 facettes colorées'

    :Returns:
        ({String|None}, {None|List}, {None|Cube})
        (erreur, liste des mouvements, cube en entrée)
    """
    err, cube_lu = lecture_cube(cube_c54)
    if err:
        return err, None, None
    else:
        err, mouvements = algo_cfop(cube_lu.copy())
        return (err, None, None) if err \
            else (None, mouvements, cube_lu)

if __name__=="__main__":
    """
    :Example:
        python poqb.py
        python poqb.py -cYYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW
        python poqb.py --cube=YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW
    """

    #On récupère le cube en paramètre ou on utilise celui par défaut
    params = readArgs()
    cube = str(params['cube']) if 'cube' in params else DEFAULT_CUBE

    err, resolution, cube_lu = solve_full(cube)
    if err:
        print("Erreur dans la lecture du cube : " + err)
    else:
        #L'utilisateur a demandé la résolution pas à pas
        if 'tuto' in params:
            print('Résolution de :', "".join([colorize(x) for x in cube]))
            tuto(cube_lu, resolution)

        print('Résolution de :', "".join([colorize(x) for x in cube]) +'\n')
        resolution = " ".join([translate_mvt(x) for x in resolution])
        print('Positionnez la face bleue face à vous et la face blanche face au sol\n')
        print("Puis exécutez la manoeuvre : {}".format(resolution) +'\n')


