# Test Polinomio Minimos Cuadrados
import unittest
import numpy as np
from src.poliMiniCuadrados import PolinomioMinimosCuadrados

class TestPolinomioMinimosCuadrados(unittest.TestCase):
    def test_ajuste(self):
        x_data = np.array([0, 1, 2, 3, 4])
        y_data = np.array([1.1, 3.5, 2.8, 4.2, 5.0])
        polinomio = PolinomioMinimosCuadrados(grado=2, x_data=x_data, y_data=y_data)
        x_vals = np.linspace(0, 4, 100)
        y_vals = polinomio.ajustar(x_vals)
        self.assertEqual(len(y_vals), len(x_vals))

if __name__ == '__main__':
    unittest.main()
