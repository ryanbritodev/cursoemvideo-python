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
