# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:45:08 2023

@author: sanaz
"""

from saturation_stockage_moyenne import taille_pop_arrondie
from scipy.integrate import solve_ivp
import numpy as np


import matplotlib.pyplot as plt

# Constantes du système
K = 95  # capacité limite du milieu
r0 = 0.03  # Taux d'accroissement de la population


# Définition de l'équation différentielle
def equation(t, x):
    return r0 * x * (1 - x / K)


t0 = 0
tf = 300  # seconde
x0 = 20  # Condition initiale
temps = 0
tempsL = []
for k in range(len(taille_pop_arrondie)):
    temps += 0.1
    tempsL += [temps]

# Résolution
solution = solve_ivp(equation, [t0, tf], [x0])

# Tracé de l'évolution de la taille d'une population

plt.plot(tempsL, taille_pop_arrondie)
plt.plot(solution.t, solution.y[0], label="x(t)")
plt.ylabel("N(t) taille de la population ou Biomass")
plt.xlabel("Temps (s)")
plt.title("Evolution d'une population")
plt.grid(which="both")
plt.legend()
plt.show()
