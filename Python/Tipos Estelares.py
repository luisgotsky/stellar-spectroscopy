import matplotlib.pyplot as plt
import numpy as np

L0 = 4
error = 3*0.03
nombres, lums = [], []

file = open("dataF", "r", encoding="utf8")

file.readline()

for linea in file:
    
    l = linea.split()
    nombres.append(l[0])
    lums.append(float(l[1]))

plt.figure(figsize=(9, 6))
plt.scatter(0, L0)
plt.grid()

for i in range(len(lums)):
    
    plt.plot([-1, 1], [lums[i], lums[i]], "--", label=nombres[i])
    
plt.ylabel("$L(L_{\\odot})$")
plt.legend()
plt.title("Estrella problema 3")
#plt.savefig("TipoF.png", dpi=200)

plt.figure(figsize=(9, 6))
plt.grid()
plt.scatter(9500, 65*3.8e33)
plt.scatter(30000, 46700*3.8e33)
plt.scatter(7200, 4*3.8e33)
plt.xlabel("$T_{eff} (K)$")
plt.ylabel("$L(erg*s^{-1})$")

Ts = np.linspace(5000, 31000, 1000)
L = lambda r: 3.8e33*(r**2)*((Ts/5777)**4)
rs = [1.28, 2.99, 8.01]

for R in rs:
    
    plt.plot(Ts, L(R), "--", label="R = " + str(R) + "$R_{\\odot}$")
    
plt.legend()
plt.savefig("TL.png", dpi=200)