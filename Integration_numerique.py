import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


# Méthode des trapèzes:
def integrale(
        f,  # Fonction (fonction intégrande, fonction à intégrer).
        a,  # Borne inférieure de l'intégrale.
        b,  # Borne supérieure de l'intégrale.
        h): # Pas de temps, valeur de l'intervalle entre tous les points auxquels on évalue la fonction.
    
    # if a > b :
    #     raise ValueError("borne inférieure plus grande que borne supérieure")
    
    valeurs = np.arange(a, b, h)  # On détermine toutes les valeurs sur lesquelles on va évaluer la fonction.
    x = valeurs
    y = f(x)
    aire = 0
    F = [0]
    for indice, element in enumerate(x[:-1]):
        aire_trapeze = h/2 * (y[indice] + y[indice + 1])
        aire += aire_trapeze
        F.append(aire)

    F = np.array(F)
    return aire






# def update(txtbox):
#     global coloriage  # Déclarer comme variable globale
    
#     try:
#         a_new = float(borne_a.text)
#         b_new = float(borne_b.text)
        
#         if a_new >= b_new:
#             print("Erreur: borne inférieure doit être < borne supérieure")
#             return

#         aire, a, b, x, y, F = integrale(lambda x: 1/(6*(15+0.14*x)), 
#                                             a_new, 
#                                             b_new, 
#                                             0.01)
#         if coloriage in ax1.collections:
#             coloriage.remove()
        
#         line1.set_data(x, y)
#         coloriage = ax1.fill_between(x, y, where=(x>=a) & (x<=b), color="skyblue", alpha=0.3)
#         ax2.legend([f"Aire = Intégrale = {aire:.4f}"])
#         line2.set_data(x, F)

#         for i in [ax1, ax2]:
#             i.relim()
#             i.autoscale_view()
        
#         fig.canvas.draw_idle()

#     except ValueError as e:
#         print(f"Erreur {e}")


# borne_a.on_submit(update)
# borne_b.on_submit(update)
# plt.show()




