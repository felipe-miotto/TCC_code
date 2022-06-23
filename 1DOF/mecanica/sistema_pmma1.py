import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


class sistema_pmma1():
    """Representação de um sistema com 1 grau de liberdade
    e amortecimento proporcional.
    """

    def __init__(self, m1, k1, beta):
        self.m1 = m1
        self.k1 = k1
        self.a1 = (beta*k1)
        self.w0 = 0
        self.Modes = []
        self.GenMass = []
        self.GenStiff = []

    def show(self):
        print(f"Massa: {self.m1}\n")
        print(f"Rigidez: {self.k1}\n")
        print(f"Amortecimento: {self.a1}")

    def resonances(self, interval):
        f = lambda w: (-w**2*self.m1 + self.k1)
        domain = np.arrange(0, interval)
        roots = []

        for bogey in domain:
            new_root = round(abs(fsolve(f, bogey)[0]), 2)
            if new_root not in roots:
                roots.append(new_root)
        return np.sort(roots)
