from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Constantes du système
K = 40  # capacité limite du milieu
r0 = -0.3  # Taux d'accroissement de la population
x_s = 20
r = 10


# Définition de l'équation différentielle
def equation(t, x):
    return r * x * (1 - (x / K)) * ((x - x_s) / (x - (x_s * r / r0)))


t0 = 0
tf = 100  # seconde
x0 = 30  # Condition initiale

# Résolution
solution = solve_ivp(equation, [t0, tf], [x0])

# Tracé de l'évolution de la taille d'une population
plt.plot(solution.t, solution.y[0], label="x(t)")
plt.ylabel("x(t) taille de la population ou Biomass")
plt.xlabel("Temps (s)")
plt.title(
    "Evolution d'une population lorsqu'un effet allee est présent dans sa dynamique"
)
plt.grid(which="both")
plt.legend()
plt.show()
