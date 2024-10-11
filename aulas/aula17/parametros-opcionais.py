# As variáveis são copiadas para os escopos da função em ordem
# somar(3, 2, 5)
# A recebe 3
# B recebe 2
# C recebe 5

# Caso B não receba nenhum valor, atribuimos a ele o número zero
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    Função criada por Ryan Brito
    """
    s = a + b + c
    print(f"A soma vale {s}")


somar(1, 4)

print()

# Um bom exemplo de um parâmetro opcional em Python é a quebra de linha
# utilizada pelo print, que é feita pela predefinição do end="" como \n

help(somar)


somar(c=2, b=2)
