# Trazador Cubico
import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt

class TrazadorCubico:
    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data
        self.spline = spi.CubicSpline(x_data, y_data, bc_type='clamped')

    def interpolar(self, x_vals):
        return self.spline(x_vals)

    def graficar(self, x_vals):
        y_vals = self.interpolar(x_vals)
        plt.plot(self.x_data, self.y_data, 'o', label="Puntos de control")
        plt.plot(x_vals, y_vals, '-', label="Trazador cúbico")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Método de Trazador Cúbico Sujeto")
        plt.show()
