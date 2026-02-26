import math
import numpy as np


def bissection(
        x1: float,                          # Valeur inférieure de l'intervalle initial.
        x2: float,                          # Valeur supérieure de l'intervalle initial.
        g: callable,                        # Fonction. On exprime g où g(x) = 0.
        n: int,                             # Nombre maximal d'itérations qu'on souhaite.
        e_max: float                        # Précision minimale (par exemple, pour e_max = 1e-5, les itérations arrêteront si la valeur de l'erreur est plus petite que 0.00005)
        ):
    
    itération = 0
    erreur = abs(x2-x1)
    while itération < n and erreur > e_max:
        x_m = (x1 + x2) / 2
        erreur = abs(x2-x_m)
        if (g(x_m)) * (g(x2)) < 0:
            x1 = x_m                        # On redéfinit le prochain intervalle comme le demi-intervalle de droite.
        else:
            x2 = x_m                        # On redéfinit le prochain intervalle comme le demi-intervalle de gauche.
        itération += 1
    return itération, x_m





# INSÉRER LES PARAMÈTRES ICI
# nombre_ité, valeur = bissection(
#                                 x1 = 0,
#                                 x2 = 1, 
#                                 g  = lambda r : 1.5 - r**2 / np.sqrt((1-r**2)**2 + (2*0.1*r)**2), 
#                                 n =  1000, 
#                                 e_max = 1e-5
#                                 )
# print("-"*30)
# print(f"{"Nombre d'itérations":<25}{"Valeur finale":<30}")
# print("-"*30)
# print(f"{nombre_ité:<25}{valeur:<30}")



