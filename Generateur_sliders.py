from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

def gen_sliders(figure:plt.figure, *sliders ):
    """
    Docstring for gen_sliders
    
    :param sliders: Description

    param_sliders est un tuple de tuples: 
                [
                    str,
                    float,
                    float,
                    float
                    
                ]
    """
    n = len(sliders)
    liste_sliders = []
    axes = [None for _ in range(n)]
    distance_entre_sliders = (1 - 0.2) / n
    for i, s in enumerate(sliders):
        axes[i] = figure.add_axes([0.05, .8 - distance_entre_sliders*i, 0.15, 0.05])
        liste_sliders.append(
            Slider(
                ax=axes[i],
                label=s[0],
                valmin=s[1],
                valmax=s[2],
                valinit=s[3]
                )
                            )
    
    return liste_sliders
    
    

