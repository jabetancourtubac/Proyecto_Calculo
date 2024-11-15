# Polinomio Minimos Cuadrados
import numpy as np
import matplotlib.pyplot as plt

class PolinomioMinimosCuadrados:
    def __init__(self, grado, x_data, y_data):
        self.grado = grado
        self.x_data = x_data
        self.y_data = y_data
        self.coeficientes = np.polyfit(x_data, y_data, grado)

    def ajustar(self, x_vals):
        polinomio = np.poly1d(self.coeficientes)
        return polinomio(x_vals)

    def graficar(self, x_vals):
        y_vals = self.ajustar(x_vals)
        plt.plot(self.x_data, self.y_data, 'o', label="Datos experimentales")
        plt.plot(x_vals, y_vals, '-', label="Ajuste de mínimos cuadrados")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Polinomio de Mínimos Cuadrados")
        plt.show()
