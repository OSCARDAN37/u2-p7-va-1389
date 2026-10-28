import numpy as np
import matplotlib.pyplot as plt
# Oscar Flores NC = 1389
No_lista = [1,2,3,17,48]
califa_ml = [20,30,80,100,90]
califa_va = [70,90,60,90,100]

plt.plot(No_lista, califa_ml, label='Califa ML')
plt.plot(No_lista, califa_va, label='Califa VA')

plt.title("Calificaciones materias 1389")
plt.xlabel("Numero de lista")
plt.ylabel("Calificacion")

plt.legend()
plt.show()