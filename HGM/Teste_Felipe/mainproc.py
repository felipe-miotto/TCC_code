##############################################################################
# Importações

import numpy as np
from mecanica.metodos_inversos import Equacao1Grau as eq1

##############################################################################
# Código principal


def main():

    equacao = eq1(1, 2)

    equacao.a = 2
    print("O parametro A eh:" + str(equacao.a))

    r = equacao.interpolar(3)
    print("O resultado da minha equação de 1 grau \
        para o parametro 3 eh: " + str(r))

    integral = equacao.integrar(0, 10)
    print("Integrar para os valores 0 e 10: " + str(integral))

    # O ultimo erro cometido:
    print("O meu erro eh: " + str(equacao.getError()))

    print(np.diag([10, 12, 13]))

##############################################################################
# Chamada em linha de comando: código principal


if __name__ == "__main__":
    main()
