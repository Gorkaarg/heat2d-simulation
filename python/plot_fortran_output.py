import numpy as np
import matplotlib.pyplot as plt

# Cargar datos del archivo generado por Fortran
data = np.loadtxt("C:/Users/Gorka/heat2d-simulation/fortran/heat2d_fortran_output.dat")



x = data[:, 0]
y = data[:, 1]
u = data[:, 2]

# Deducir dimensiones de la malla
Nx = len(np.unique(x))
Ny = len(np.unique(y))

X = x.reshape(Ny, Nx)
Y = y.reshape(Ny, Nx)
U = u.reshape(Ny, Nx)

plt.figure(figsize=(6, 5))
plt.imshow(U, cmap="hot", origin="lower",
           extent=[X.min(), X.max(), Y.min(), Y.max()])
plt.colorbar(label="Temperatura")
plt.title("Solución 2D de la ecuación de calor (Fortran)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
