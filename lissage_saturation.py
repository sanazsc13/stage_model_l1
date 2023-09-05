# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:19:57 2023

@author: sanaz
"""

from modèle_stochastique_finale import mega_fonction
import numpy as np
import matplotlib.pyplot as plt
import statistics

M = np.array(mega_fonction()[0])
moyenne_taille_popL = []
for j in range(20):
    M = np.vstack([M, mega_fonction()[0]])
for i in range(len(M.T)):
    moyenne_taille_popL += [np.mean(M[:, i])]
res = 0
c = 0
#for k in moyenne_taille_popL[1000:]:
 #   res += k
#    c += 1
K = res / c
print(K)
tempsL = mega_fonction()[1]
plt.plot(tempsL, moyenne_taille_popL[:-1])
plt.show()

# M = np.array([0,1,2])
# K = []
# for k in range(3):
#   M =np.vstack([M,[0,2,5]])
# for u in range(len(M.T)):
#    K +=[ np.mean(M[:,u])]
# print(K, M.shape, len(M.T), M)
