#Import des packages utilisés par la fonction
import numpy as np
from enum import Enum

class Strategie(Enum):
    CHANGER = 1
    GARDER = 2



def play_all(strategie, nb_parties):

    # Portes au choix : porte 0, porte 1 ou porte 2
    portes = np.tile([[0,1,2]], (nb_parties,1))
    
    # Porte avec la bonne réponse
    bonne_porte = np.random.randint(0,3, size = nb_parties)
    bonne_porte = np.reshape(bonne_porte, (-1,1))
    
    # Choix du joueur
    premier_choix = np.random.randint(0,3, size = nb_parties)
    premier_choix = np.reshape(premier_choix, (-1,1))
    
    # Il reste 2 portes après le choix du joueur
    Porte_a_retirer = portes == premier_choix
    mask_portes = np.ma.array(portes, mask=Porte_a_retirer)
    portes = mask_portes.compressed()
    portes = np.reshape(portes, (-1,2))

    
    # Selection d'une porte au hasard sur les 2 dernières portes
    a = np.random.choice(a=[False, True], size=nb_parties)
    b = np.logical_not(a)
    Porte_a_retirer = np.vstack((a, b)).T
    
    mask_portes = np.ma.array(portes, mask=Porte_a_retirer)
    porte_restante = mask_portes.compressed()
    porte_restante = np.reshape(porte_restante, (-1,1))
    
    # Le présentateur élimine une des deux portes restantes  
    porte_restante = np.where(bonne_porte == premier_choix, porte_restante, bonne_porte)

    # Initialisation du deuxième choix
    deuxieme_choix = np.zeros((nb_parties, 1))
    
    # Le deuxieme choix depend de la strategie
    if strategie.value == Strategie.CHANGER.value:
        deuxieme_choix = porte_restante
    elif strategie.value == Strategie.GARDER.value:
        deuxieme_choix = premier_choix
    else:
        raise ValueError("Stratégie non reconnue!")
    
    return deuxieme_choix == bonne_porte
