from saturation_stockage_moyenne import taille_pop_arrondie
import numpy as np
import matplotlib.pyplot as plt

N_0 = 20
K = 95


# def fonction_transfo(N):
#     premier_membre = np.log((1 / N) - (1 / K))
#     second_membre = np.log((1 / N_0) - (1 / K))
#     y = premier_membre - second_membre
#     return y


# for u in range(len(taille_pop_arrondie)):
#     taille_pop_transfo += []


def fonction_tfo(r_0):
    taille_pop_transfo = []
    tempsL = []
    res = 0
    temps = 0
    for i in range(len(taille_pop_arrondie)):
        temps += 0.1
        tempsL += [temps]
        res += (
            ((K * N_0) / (N_0 + (K - N_0) * np.exp(-r_0 * temps)))
            - taille_pop_arrondie[i]
        ) ** 2
    return res


fonction_tfoL = []
r_0L = []
r_0 = 0
for k in range(20):
    r_0 += 0.01
    r_0L += [r_0]
    fonction_tfoL += [fonction_tfo(r_0)]

print(
    fonction_tfoL.index(min(fonction_tfoL)),
    r_0L[fonction_tfoL.index(min(fonction_tfoL))],
)
# plt.plot(r_0L, fonction_tfoL)
# plt.show()
