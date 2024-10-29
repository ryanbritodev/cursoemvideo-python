def aumentar(valor, porcentagem, formatar=False):
    if formatar:
        return "R${:.2f}".format(valor + valor * (porcentagem / 100)).replace(".", ",")
    return valor + valor * (porcentagem / 100)


def diminuir(valor, porcentagem, formatar=False):
    if formatar:
        return "R${:.2f}".format(valor - valor * (porcentagem / 100)).replace(".", ",")
    return valor - valor * (porcentagem / 100)


def dobro(valor, formartar=False):
    if formartar:
        return "R${:.2f}".format(valor * 2).replace(".", ",")
    return valor * 2


def metade(valor, formartar=False):
    if formartar:
        return "R${:.2f}".format(valor / 2).replace(".", ",")
    return valor / 2


def moedas(valor):
    return "R${:.2f}".format(valor).replace(".", ",")


def resumo(valor, aumento, reducao):
    valorAumento = aumentar(valor, aumento, True)
    valorReducao = diminuir(valor, reducao, True)
    valorMetade = metade(valor, True)
    valorDobro = dobro(valor, True)
    valorFormatado = moedas(valor)
    print("-" * 30)
    print("{:^30}".format("RESUMO DO VALOR"))
    print("-" * 30)
    print("Preço analisado: {:>13}".format(valorFormatado))
    print("Dobro do Preço: {:>14}".format(valorDobro))
    print("Metade do Preço: {:>13}".format(valorMetade))
    print("{:<2}% de aumento: {:>14}".format(aumento, valorAumento))
    print("{:<2}% de redução: {:>14}".format(reducao, valorReducao))
    print("-" * 30)
