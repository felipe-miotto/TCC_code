class sistema_pmma1():
    """Representação de um sistema com 1 grau de liberdade
    e amortecimento proporcional.
    """


def __init__(self, m1, k1, beta):
    self.m1 = m1
    self.k1 = k1
    self.a1 = (beta*k1)


def show(self):
    print(f"Massa: {self.m1}\nRigidez: {self.k1}\nAmortecimento: {self.a1}")
