import matplotlib.pyplot as plt
import numpy as np

x_s = int(input("Choisir x_s strictement négatif: "))
r = int(input("Choisir r strictement positif: "))
K = int(input("Choisir K  strictement positif et supérieur que x_s: "))
r0 = int(input("Choisir r_o sstrictement positif: "))


x = np.linspace(0, 1000, 100)
y = r * (1 - (x / K)) * ((x - x_s) / K)
plt.title("Courbe de la fonction F(x) représentative de l'effet allee faible ")
plt.xlabel("x")
plt.ylabel(" F(x)")
plt.plot(x, y, alpha=0.4, color="yellow", linestyle="dashed", linewidth=2)
plt.grid(alpha=0.6, linestyle="-")
plt.plot(x, y, "y", label="F(x)=r * (1 - (x / K))*((x - x_s) / K)")
# Placer la lagénde
plt.legend(loc="upper left")
plt.show()
