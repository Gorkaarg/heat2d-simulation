import numpy as np
import matplotlib.pyplot as plt
import os

# ============================
# Parámetros de la simulación
# ============================

Lx = 1.0          # Longitud en x
Ly = 1.0          # Longitud en y
Nx = 50           # Número de puntos en x
Ny = 50           # Número de puntos en y
alpha = 1.0       # Difusividad térmica
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

# Condición de estabilidad (FTCS)
dt = 0.25 * min(dx, dy)**2 / alpha
Nt = 300          # Número de pasos temporales

# ============================
# Malla y condición inicial
# ============================

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Condición inicial: un "hot spot" en el centro
u = np.exp(-50 * ((X - 0.5)**2 + (Y - 0.5)**2))

# ============================
# Función para un paso FTCS
# ============================

def step_ftcs(u):
    un = u.copy()
    u[1:-1, 1:-1] = (
        un[1:-1, 1:-1]
        + alpha * dt * (
            (un[2:, 1:-1] - 2*un[1:-1, 1:-1] + un[:-2, 1:-1]) / dx**2 +
            (un[1:-1, 2:] - 2*un[1:-1, 1:-1] + un[1:-1, :-2]) / dy**2
        )
    )
    return u

# ============================
# Visualización
# ============================

plt.ion()
fig, ax = plt.subplots(figsize=(6, 5))

for n in range(Nt):
    u = step_ftcs(u)

    if n % 20 == 0:
        ax.clear()
        c = ax.imshow(u, cmap='hot', origin='lower', extent=[0, Lx, 0, Ly])
        ax.set_title(f"Paso temporal n = {n}")
        fig.colorbar(c, ax=ax)
        plt.pause(0.01)

# ============================
# Guardar resultado final
# ============================

if not os.path.exists("../plots"):
    os.makedirs("../plots")

plt.savefig("../plots/heat2d_final.png")
print("Simulación completada. Imagen guardada en plots/heat2d_final.png")
