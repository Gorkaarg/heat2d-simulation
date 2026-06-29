import numpy as np
import matplotlib.pyplot as plt
import time

# Parámetros
Nx = 50
Ny = 50
Lx = 1.0
Ly = 1.0
alpha = 1.0
Nt = 300

dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)
dt = 0.25 * min(dx, dy)**2 / alpha

# Malla
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Condición inicial
u = np.exp(-50 * ((X - 0.5)**2 + (Y - 0.5)**2))

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

# -------------------------
# MEDICIÓN DE TIEMPO PYTHON
# -------------------------
t0 = time.time()

for n in range(Nt):
    u = step_ftcs(u)

t1 = time.time()
print("Tiempo Python:", t1 - t0, "segundos")

