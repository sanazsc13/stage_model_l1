import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

n_0 = 20
l_x = 1
l_y = 1
constante_mortalité = 0.01
intervalle = 100
delta_t = 0.01
mu0 = 0.1
lambda_reproduction = 0.4
sigma_m = 0.12
sigma_w = 0.12
constante_mort = constante_mortalité * (1 / (sigma_w * np.sqrt(2 * np.pi)))

# INITIALISATION DU SYSTEME
taille_pop = n_0
taille_popL = []
mort_indiceL = []
tempsL = []
temps = 0
x_yL = []
nb_pas_temps = int(intervalle / delta_t)
# Initialisation du système
for i in range(taille_pop):
    x_yL += [[np.random.uniform(0, l_x), np.random.uniform(0, l_y)]]
taille_popL += [taille_pop]


def bernouilli(p):
    proba = np.random.uniform(0, 10)
    if proba < p:
        return True
    else:
        return False


#   EVALUATION DE LA COMPETITION POUR CHAQUE INDIVIDU


def competition(individu):
    x = x_yL[individu][0]
    y = x_yL[individu][1]
    risque_total = 0
    for i in range(len(x_yL)):
        if i != (individu):
            x_compet = x_yL[i][0]
            y_compet = x_yL[i][1]
            distance_x = min(
                abs(x - x_compet), abs(l_x - max((x - x_compet), (x_compet - x)))
            )
            distance_y = min(
                abs(y - y_compet), abs(l_y - y + y_compet), abs(l_y - y_compet + y)
            )
            risque = np.exp(-(distance_x**2) / (2 * (sigma_w**2))) * np.exp(
                (-(distance_y**2) / (2 * (sigma_w**2)))
            )
        else:
            risque = 0
        risque_total += risque
    return constante_mort * risque_total


def reproduction(individu):
    repro = 0
    x = x_yL[individu][0]
    y = x_yL[individu][1]
    c = 0
    for j in range(len(x_yL)):
        if j != individu:
            distance_x = min(
                abs(x - x_yL[j][0]), abs(l_x - max((x - x_yL[j][0]), (x_yL[j][0] - x)))
            )
            distance_y = min(
                abs(y - x_yL[j][1]),
                abs(l_y - y + x_yL[j][1]),
                abs(l_y - x_yL[j][1] + y),
            )
            if np.sqrt(distance_x**2 + distance_y**2) < 0.01:
                c += 1
            else:
                c = c
    if c > 0:
        repro = lambda_reproduction
    else:
        repro = 0
    return repro


# ELIMINATIONN DES MORTS
def mort(L, M):
    new = []
    for f in range(len(L)):
        if f in M:
            pass
        else:
            new += [L[f]]
    return new


# DEMARRAGE DE LA SIMULATION
for itération in tqdm(range(nb_pas_temps)):
    #   BOUCLE TEMPS
    # print("t",itération, taille_popL)
    # print(taille_pop)
    for individu in range(taille_popL[itération]):
        if bernouilli(reproduction(individu) * delta_t):
            new_x = np.random.normal(x_yL[individu][0], sigma_m)
            new_y = np.random.normal(x_yL[individu][1], sigma_m)
            if new_x > l_x:
                new_x = new_x % l_x
            elif new_x < 0:
                new_x = l_x + new_x
            else:
                new_x = new_x
            if new_y > l_y:
                new_y = new_y % l_y
            elif new_y < 0:
                new_y = l_x + new_y
            else:
                new_y = new_y
            x_yL += [[new_x, new_y]]
            taille_pop += 1
        compet_tot = mu0 + competition(individu)
        # print(taille_pop, len(taille_popL), len(x_yL))
        if bernouilli(compet_tot * delta_t):
            taille_pop -= 1
            mort_indiceL += [individu]
        # print(taille_pop, len(taille_popL), len(x_yL))
    taille_popL.append(taille_pop)
    x_yL = mort(x_yL, mort_indiceL)
    temps += delta_t
    tempsL += [temps]
    mort_indiceL = []
    # print(temps)
    # print(taille_pop, len(taille_popL), len(x_yL))
    # COURBE DE REPARTITION DANS L'ESPACE ##
x = []
y = []
for j in range(len(x_yL)):
    x += [x_yL[j][0]]
    y += [x_yL[j][1]]
plt.plot(x, y, ".")
plt.show()
# print(taille_popL)
plt.plot(tempsL, taille_popL[:-1])
plt.show()
# ESTIMATION DE LA CAPACITE LIMITE##
# MOYENNE DES VALEURS
c = 0
res = 0
# for j in taille_popL[1200:]:
#     c += 1
#     res += j
# K = res / c
# return [taille_popL, tempsL]
