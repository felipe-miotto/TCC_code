# Importações #################################################################

from mecanica.sistema_pmma1 import sistema_pmma1 as pmma1


# Código Principal ###########################################################

def main():
    sistema = pmma1(79.2, 1000000, 0.0005)
    sistema.show()

    sistema2 = pmma1(15, 2500, 0.002)
    sistema2.show()

# Chamada em linha de comando do main code ###################################


if __name__ == "__main__":
    main()
