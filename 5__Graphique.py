import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from Classe_systeme import System
from Generateur_sliders import gen_sliders  


        

        



premier_tableau = System(50, 20, 10, 1000, 10, 0.1, 0.5)
r = premier_tableau.affichage()
fig, line1 = r[0], r[1]
fig.subplots_adjust(left=0.25, bottom=0.10)
slider_force, slider_omega, slider_masse, slider_raideur, slider_amortissement, slider_x_0, slider_v_0 = gen_sliders(
    r[0],
    ["F", 3, 1000, 200],
    ["w", 0, 100, 20],
    ["M", 2, 100, 10],
    ["K", 100, 10000, 1000],
    ["C", 3, 200, 10],
    ["x_0", 0, 2, 0.1],
    ["v_0", 0, 1, 0.5],
)
def update(val):                            # Fonction copiée depuis Claude.
    nouveau_systeme = System(
        slider_force.val,
        slider_omega.val,
        slider_masse.val,
        slider_raideur.val,
        slider_amortissement.val,
        slider_x_0.val,
        slider_v_0.val
    )
    nouvelles_positions = nouveau_systeme.position()
    
    # Adapter le tableau de temps (peut changer si omega change)
    line1.set_xdata(nouveau_systeme.temps)
    line1.set_ydata(nouvelles_positions)
    
    ax = r[2]  # l'axe original
    ax.relim()
    ax.autoscale_view()
    r[0].canvas.draw_idle()  # redessiner la figure    

slider_force.on_changed(update)
slider_omega.on_changed(update)
slider_masse.on_changed(update)
slider_raideur.on_changed(update)
slider_amortissement.on_changed(update)
slider_x_0.on_changed(update)
slider_v_0.on_changed(update)

    
plt.show()
