# Heat2D Simulation — Python vs Fortran

Simulación numérica de la ecuación del calor en 2D utilizando el método FTCS (Forward Time Centered Space).  
El proyecto incluye implementaciones en **Python** y **Fortran**, además de una comparación de tiempos de ejecución.

---

## 📌 Objetivos del proyecto

- Resolver la ecuación del calor en 2D con condiciones de contorno simples.
- Comparar rendimiento entre Python y Fortran.
- Generar gráficos de la evolución térmica y de los tiempos de ejecución.
- Documentar el proceso de forma clara y reproducible.

---

## 📁 Estructura del repositorio

heat2d-simulation/
│
├── python/
│   ├── heat2d_python.py
│   ├── compare_times.py
│
├── fortran/
│   ├── heat2d_fortran.f90
│   └── heat2d_fortran_output.dat
│
├── report/
│   └── compare_times.png
│
└── README.md


---

## ⚙️ Método numérico: FTCS

El método FTCS discretiza la ecuación del calor:



\[
\frac{\partial T}{\partial t} = \alpha \left( 
\frac{\partial^2 T}{\partial x^2} +
\frac{\partial^2 T}{\partial y^2}
\right)
\]



Usando diferencias finitas:



\[
T_{i,j}^{n+1} = T_{i,j}^n + \lambda \left(
T_{i+1,j}^n + T_{i-1,j}^n +
T_{i,j+1}^n + T_{i,j-1}^n -
4T_{i,j}^n
\right)
\]



donde:

- \(\lambda = \alpha \frac{\Delta t}{\Delta x^2}\)
- Condición de estabilidad: \(\lambda \le 0.25\)

---

## 🚀 Ejecución

### Python

```bash
python python/heat2d_python.py


---

### Fortran

Compilar: gfortran fortran/heat2d_fortran.f90 -o heat2d
Ejecutar: ./heat2d

Comparación de tiempos
El script compare_times.py mide el tiempo de ejecución de ambos programas y genera un gráfico comparativo.

Resultados
Python: ~0.01176 s

Fortran: ~0.00564 s

Fortran es aproximadamente 2× más rápido en esta implementación.

##Trabajo futuro
###Implementación paralela con MPI.
###Comparación con mallas más grandes.
###Animación de la evolución térmica.
###Optimización de memoria y vectorización en Fortran.

##Autor
Gorka — UPV/EHU
Proyecto académico de simulación numérica