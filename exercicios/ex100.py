from random import randint

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def sorteiaCinco(lista):
    tamanhoLista = len(lista)
    if tamanhoLista < 5:
        return print("Você não pode ter menos de 5 termos!")
    else:
        numerosAleatorios = []
        for i in range(1, 6):
            numeroAleatorio = randint(0, len(lista) - 1)
            numero = lista[numeroAleatorio]
            if numero in numerosAleatorios:
                while numero in numerosAleatorios:
                    numeroAleatorio = randint(0, len(lista) - 1)
                    numero = lista[numeroAleatorio]
                    if numero not in numerosAleatorios:
                        break
                    else:
                        continue
            numerosAleatorios.append(numero)
    return numerosAleatorios


numerosSorteados = sorteiaCinco(numeros)
print(numerosSorteados)


def somaPar(lista):
    somador = 0
    for i in lista:
        if i % 2 == 0:
            somador += i
        else:
            continue
    return somador


print(somaPar(numerosSorteados))
