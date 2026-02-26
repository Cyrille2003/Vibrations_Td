from matplotlib.widgets import Slider
from Generateur_sliders import gen_sliders
from Newton_1D import Newton, derivee_locale
from Integration_numerique import integrale
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pi = np.pi
sin = np.sin
cos = np.cos
sqrt = np.sqrt
atan = np.atan
exp = np.exp
class System():
    def __init__(self, F, w, m, k, c, x_0, v_0, h=1e-5):
        self.F = F
        self.w = w
        self.m = m
        self.k = k
        self.c = c
        self.x_0 = x_0
        self.v_0 = v_0
        self.h = h

        self.w_n = sqrt(k/m)
        self.cc = 2 * sqrt(k*m)
        self.zeta = c / self.cc
        self.w_d = self.w_n * sqrt(1- self.zeta**2)
        self.phi = atan(self.c * self.w / (self.k - self.m * self.w**2))

        temps = 2 * pi / w * 30
        self.temps = np.arange(0, temps, h)
        self.X = self.F / (sqrt((self.k - self.m*self.w**2)**2 + (self.c * self.w)**2))
        self.tho_d = 2*pi / self.w_d


    def position(self):
        B1 = (self.v_0 + self.zeta * self.w_n * self.x_0) / self.w_d
        B2 = self.x_0

        solution_homogene = self.X*sin(self.w * self.temps + self.phi)
        solution_particuliere = (B1 * sin(self.w_d * self.temps) + B2 * cos(self.w_d * self.temps)) * exp(-self.zeta * self.w_n * self.temps)
        solution_totale = solution_particuliere + solution_homogene
        return solution_totale
    
    def affichage(self):
        fig, axes = plt.subplots(1,1)
        line1, = axes.plot(self.temps, self.position())
        return fig, line1, axes
    
    def vitesse(self):
        positions = self.position()
        vit = []
        for i, p in enumerate(positions[1:]):
            v = (p - positions[i])/self.h
            vit.append(v)

        return np.array(vit)
    
    def acceleration(self):
        vitesses = self.vitesse()
        acc = []
        for i, v in enumerate(vitesses[1:]):
            a = (v - vitesses[i])/self.h
            acc.append(a)

        return np.array(acc)
    
    def verif(self):
        """
        Problèmes avec cette fonction : 
        1. Comme la discrétisation est très petite (1e-5), les sommets où v=0 peuvent être nombreux pour un même sommet. 
        Et le paramètre de test avec v < 1e-4 n'est pas effectif pour isoler le vrai sommet.
        Par conséquent, il faut ajouter une condition pour que ce soit un vrai sommet. Et qu'on puisse donc trouver 3 vrais sommets équivalents de suite.
        Pour ce faire, je propose d'ajouter la condition suivante : 
            v[i-1] < v[i] > v[i+1]
        
        2. La valeur qui fait que les sommets sont identiques devrait être un pourcentage de l'amplitude (plutôt qu'une valeur définie comme 1e-4)
        Comme ça, on pourra avoir un critère juste et équitable pour tous les systèmes, peu importe leurs paramètres.
        """
        # a_max = abs(-self.X * self.w**2)
        # a = self.acceleration()
        pos = self.position()
        vit = self.vitesse()
        liste_temps_peaks = []
        liste_peaks = []
        for i in range(1, len(pos)):
            if pos[i] < 0:
                continue
            if vit[i-1] < 1e-5:
                liste_peaks.append(pos[i])
                liste_temps_peaks.append(i*self.h)
        
        compteur = 0
        for i in range(1, len(liste_temps_peaks)):
            if liste_temps_peaks[i] - liste_temps_peaks[i-1] - self.tho_d < 0.01 and liste_peaks[i] - liste_peaks[i-1] < 1e-3:
                compteur += 1
                if compteur == 3:
                    return liste_temps_peaks[i]
            else:
                compteur = 0

        
    def td_analytique(self):
        eq1 = lambda t: np.trapezoid(self.c * (self.X*self.w*cos(self.w*np.arange(t, t+self.tho_d, self.h)+self.phi))**2, dx=1e-5) - np.trapezoid(self.F * sin(self.w*np.arange(t, t+self.tho_d, self.h)) * self.X*self.w*cos(self.w*np.arange(t, t+self.tho_d, self.h) + self.phi), dx=self.h)

        return Newton(x0=2 * pi / self.w * 30, fonction=eq1)
        




system1 = System(50, 20, 10, 1000, 10, 0.1, 0.5)
print(system1.td_analytique())
# ORDRES DE GRANDEUR ENRE 0 et 1.
# Se documenter sur la régression linéaire et non linéaire
# Support vector machine. (non linéaire)
# 1000 points de données minimum.


