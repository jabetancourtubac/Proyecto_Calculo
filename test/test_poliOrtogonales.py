# Test Polinomios Ortogonales
import unittest
import numpy as np
from src.poliOrtogonales import PolinomiosOrtogonales

class TestPolinomiosOrtogonales(unittest.TestCase):
    def test_evaluacion(self):
        polinomio = PolinomiosOrtogonales(grado=2)
        x_vals = np.linspace(-1, 1, 100)
        y_vals = polinomio.evaluar(x_vals)
        self.assertEqual(len(y_vals), len(x_vals))

if __name__ == '__main__':
    unittest.main()
