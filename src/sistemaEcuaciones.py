# Sistema ecuaciones
import numpy as np

class SistemaEcuaciones:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def resolver(self):
        return np.linalg.solve(self.A, self.b)
