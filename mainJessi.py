
import numpy as np #hace calculos
import pandas as pd #lee los archivos csv
from src.trazadorCubico import TrazadorCubico
from src.poliMiniCuadrados import PolinomioMinimosCuadrados
from src.poliOrtogonales import PolinomiosOrtogonales
from src.sistemaEcuaciones import SistemaEcuaciones

def cargar_datos_trazador():
    datos = pd.read_csv("datos/trazador_cubico_datos.csv")
    return datos["x_data"].values, datos["y_data"].values

def cargar_datos_minimos_cuadrados():
    datos = pd.read_csv("datos/minimos_cuadrados_datos.csv")
    return datos["x_data"].values, datos["y_data"].values

def cargar_datos_sistema_ecuaciones():
    datos = pd.read_csv("datos/sistema_ecuaciones_datos.csv", header=None)
    A = datos.iloc[:, :-1].values  # Las primeras columnas son A
    b = datos.iloc[:, -1].values   # La última columna es b
    return A, b

def main():

    # Trazador Cúbico Sujeto
    print("Ejecutando el método de trazador cúbico sujeto...")
    x_data_trazador, y_data_trazador = cargar_datos_trazador()
    x_vals_trazador = np.linspace(0, 5, 100)
    
    trazador = TrazadorCubico(x_data_trazador, y_data_trazador)
    trazador.graficar(x_vals_trazador)

    # Polinomio de Mínimos Cuadrados
    print("Ajustando el polinomio de mínimos cuadrados...")
    x_data_minimos, y_data_minimos = cargar_datos_minimos_cuadrados()
    x_vals_minimos = np.linspace(0, 4, 100)
    
    polinomio_minimos = PolinomioMinimosCuadrados(grado=2, x_data=x_data_minimos, y_data=y_data_minimos)
    polinomio_minimos.graficar(x_vals_minimos)

    # Polinomios Ortogonales
    print("Evaluando polinomio ortogonal de Legendre...")
    grado_legendre = 3
    x_vals_legendre = np.linspace(-1, 1, 100)
    
    polinomios_ortogonales = PolinomiosOrtogonales(grado=grado_legendre)
    polinomios_ortogonales.graficar(x_vals_legendre)

    # Resolución de Ecuaciones Lineales
    print("Resolviendo el sistema de ecuaciones lineales...")
    A, b = cargar_datos_sistema_ecuaciones()
    
    sistema = SistemaEcuaciones(A, b)
    soluciones = sistema.resolver()
    print("Soluciones del sistema de ecuaciones:", soluciones)

if __name__ == "__main__":
    main()
