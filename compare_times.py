import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Tiempos reales medidos
tiempo_python = 0.011763811111450195
tiempo_fortran = 0.00564

lenguajes = ["Python", "Fortran"]
tiempos = [0.011763811111450195, 0.00564]

plt.figure(figsize=(8,5))
plt.bar(lenguajes, tiempos, color=["orange", "blue"])
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de tiempos: Python vs Fortran (Gorka)")

# Ajuste automático del eje Y para que ambas barras sean visibles
plt.ylim(0, max(tiempos) * 1.3)

# Etiquetas con formato claro
for i, t in enumerate(tiempos):
    plt.text(i, t + max(tiempos)*0.05, f"{t:.6f} s", ha="center")

plt.show()

plt.savefig("compare_times.png")
