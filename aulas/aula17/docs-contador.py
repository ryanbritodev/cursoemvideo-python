# Exemplo de uma Docstring

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Ryan Brito
    """
    c = i
    while c <= f:
        print(f'{c}', end="... ")
        c += p
    print("FIM!")


contador(1, 15, 1)

help(contador)
