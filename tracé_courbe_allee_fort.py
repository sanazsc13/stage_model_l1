import matplotlib.pyplot as plt
import numpy as np

x_s = int(
    input(
        "Choisir x_s, densité critique en dessous de laquelle r0 est négatif strictement positif et inférieur à K: "
    )
)
r = int(input("Choisir r strictement positif: "))
K = int(input("Choisir K  strictement positif et supérieur que x_s: "))
r0 = float(input("Choisir r_o sstrictement négatif: "))

# print((r + (x_s * r**2)) / (r0))

x = np.linspace(0, 3000, 1000)
y1 = r * (1 - (x / K)) * ((x - x_s) / (x - ((x_s * r) / r0)))
y2 = ((-r * x) / K) + r - (r / K)
plt.title("Courbe de la fonction F(x) représentative de l'effet allee fort")
plt.xlabel("x")
plt.ylabel(" F(x)")
plt.plot(x, y1, alpha=0.4, color="yellow", linestyle="dashed", linewidth=2)
plt.plot(x, y2)
plt.grid(alpha=0.6, linestyle="-")
plt.plot(
    x, y1, "y", label="F(x)=r * (1 - (x / K)) * ((x - x_s) / (x - ((x_s * r) / r0)))"
)
# Placer la lagénde
plt.legend(loc="upper right")
plt.show()
