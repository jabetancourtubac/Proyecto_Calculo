# Test Sistema Ecuaciones
import unittest
import numpy as np
from src.sistemaEcuaciones import SistemaEcuaciones

class TestSistemaEcuaciones(unittest.TestCase):
    def test_resolver(self):
        A = np.array([[1, 2, 1], [2, -1, 1], [3, 1, -1]])
        b = np.array([4, 1, -2])
        sistema = SistemaEcuaciones(A, b)
        soluciones = sistema.resolver()
        self.assertEqual(len(soluciones), len(b))

if __name__ == '__main__':
    unittest.main()
