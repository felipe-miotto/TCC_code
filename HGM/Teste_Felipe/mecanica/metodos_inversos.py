from random import uniform


class Equacao1Grau():

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__bias = 0

    def interpolar(self, x):
        return (self.a)*x + (self.b) + self.__randomError()

    def getError(self):
        return self.__bias

    def integrar(self, x, y):
        return self.a*(y**2)/2 + self.b*y - self.a*(x**2)/2 - \
            self.b*x + self.__randomError()*y - self.__randomError()*x

    def __randomError(self):
        self.__bias = uniform(0, 0.01)
        return self.__bias
