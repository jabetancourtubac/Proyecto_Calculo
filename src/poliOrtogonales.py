# Polinomios ortogonales
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Legendre

class PolinomiosOrtogonales:
    def __init__(self, grado):
        self.grado = grado
        self.polinomio_legendre = Legendre.basis(grado)

    def evaluar(self, x_vals):
        return self.polinomio_legendre(x_vals)

    def graficar(self, x_vals):
        y_vals = self.evaluar(x_vals)
        plt.plot(x_vals, y_vals, '-', label=f"Polinomio de Legendre grado {self.grado}")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Polinomio Ortogonal de Legendre")
        plt.show()
