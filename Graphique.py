import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from Classe_systeme import System
from Generateur_sliders import gen_sliders  


premier_tableau = System(50, 20, 10, 1000, 10, 0.1, 0.5)
res = premier_tableau.resultats()
t, x, v, e = res["Temps"], res["Position"], res["Vitesse"], res["Énergie"]
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

line1 = ax1.plot(t, x)
line2 = ax2.plot(t, e)

ax1.set_title("Position")
ax1.set_xlabel("Temps")
ax1.set_ylabel("Position (m)")


ax2.set_title("Énergie")
ax2.set_xlabel("Temps")
ax2.set_ylabel("Énergie (Joules)")


# fig, line1 = r[0], r[1]
fig.subplots_adjust(left=0.30, bottom=0.10)
sliders = slider_force, slider_omega, slider_masse, slider_raideur, slider_amortissement, slider_x_0, slider_v_0 = gen_sliders(
    fig,
    ["F", 3, 1000, 200],
    ["w", 0, 100, 20],
    ["M", 2, 50, 10],
    ["K", 100, 10000, 1000],
    ["C", 3, 100, 10],
    ["x_0", 0, 2, 0.1],
    ["v_0", 0, 1, 0.5]
)
def update(val):                            # Fonction copiée depuis Claude.
    global vline
    
    nouveau_systeme = System(
        slider_force.val,
        slider_omega.val,
        slider_masse.val,
        slider_raideur.val,
        slider_amortissement.val,
        slider_x_0.val,
        slider_v_0.val
    )

    nouvelles_données = nouveau_systeme.resultats()
    t, x, v, e = nouvelles_données["Temps"], nouvelles_données["Position"], nouvelles_données["Vitesse"], nouvelles_données["Énergie"]
    
    # Supprimer l'ancienne ligne verticale et en créer une nouvelle
    new_td = nouveau_systeme.td_analytique()
    print(new_td)
    
    line1[0].set_xdata(t)
    line1[0].set_ydata(x)

    line2[0].set_xdata(t)
    line2[0].set_ydata(e)
    
    ax1.relim()  # l'axe original
    ax2.relim()
    ax1.autoscale_view()
    ax2.autoscale_view()
    fig.canvas.draw_idle()  # redessiner la figure    


for sl in sliders:
    sl.on_changed(update)

    
plt.show()
