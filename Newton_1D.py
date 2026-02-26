import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def derivee_locale(   
        f,            # Fonction pour laquelle on veut trouver la dérivée en x.
        h:float,      # Pas de temps pour estimer la dérivée en x.
        x:float       # x auquel on veut trouver la dérivée de f.
                ):
    return ( f(x+h) - f(x-h) ) / (2*h)



def Newton(
        x0:float,    # Valeur initiale de départ.
        fonction,    # Fonction = 0 pour laquelle on souhaite trouver le x qui résout l'équation.
        h=1e-6,           # Pas de temps pour lequel on veut effectuer le calcul de la dérivée.
        N = 40,       # Nombre d'itéations maximal.
        Precisison = 1e-12           
           ):
    
    x = [x0]
    for _ in range(N):
        if len(x) == 1:
            x_s = x[-1] - fonction(x[-1]) / derivee_locale(fonction, h, x[-1])
            x.append(x_s)
        elif len(x) >= 2 and abs(x[-1] - x[-2]) > Precisison:
            x_s = x[-1] - fonction(x[-1]) / derivee_locale(fonction, h, x[-1])
            x.append(x_s)
        if len(x) >= 2 and abs(x[-1] - x[-2]) <= Precisison:
            print(f"Nous sommes arrivés à la précision = {Precisison} désirée.")
            break
    i = len(x)
    def résultats():
        erreurs = [abs((x[_+1] - x[_]) / x[_]) for _ in range(i-1)]
        erreurs_degré_2 = [abs((x[_+1] - x[_]) / x[_]**2) for _ in range(i-2)]
        itérations = list(range(i))
        return itérations, x, erreurs, erreurs_degré_2
    res = résultats()
    res[2].append(0)
    res = pd.DataFrame({"Valeurs": res[1], "Erreur": res[2]})
    return res



# itérations, x, erreurs, erreurs_degré_2 = Newton(60, 
#                                                  fonction=lambda V: 550000 + 2.66**2 * 928/2 * V**2 - 735000 - 466*V**2, 
#                                                  h=0.001
#                                                  )      
# print('-' * 80)
# print(f"{"Itération":<12}{"x[i]":<15}{"Erreurs[i]":<12}{"Erreurs_degré_2[i]":<16}")
# print('-' * 80)
# for i, itération in enumerate(itérations[:-1]):
#     try:
#         print(f"{itération:<12}{x[i]:<15.10f}{erreurs[i]:<12.4e}{erreurs_degré_2[i]:<16.4e}")
    
#     except IndexError:
#         print(f"{itération:<12}{x[i]:<15.10f}{erreurs[i]:<12.4e}")
#         print(f"{(i+1):<12}{x[i+1]:<15.10f}")
#         print(f"Valeur finale au bout de {itération + 2} itérations : {x[-1]}")





