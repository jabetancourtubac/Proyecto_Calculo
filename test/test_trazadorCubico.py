#Test Trazador Cubico
import unittest
import numpy as np
from src.trazadorCubico import TrazadorCubico

class TestTrazadorCubico(unittest.TestCase):
    def test_interpolacion(self):
        x_data = np.array([0, 1, 2, 3, 4, 5])
        y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])
        trazador = TrazadorCubico(x_data, y_data)
        x_vals = np.linspace(0, 5, 100)
        y_vals = trazador.interpolar(x_vals)
        self.assertEqual(len(y_vals), len(x_vals))

if __name__ == '__main__':
    unittest.main()
