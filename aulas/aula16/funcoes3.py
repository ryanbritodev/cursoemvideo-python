# Empacotamento de parâmetros nas funções

# Vamos imaginar uma função que conte a quantidade de
# parâmetros em uma função, chamada contador()

# contador(5, 7, 3, 1, 4)
# Retorno deve ser 5 (5 elementos)

# * significa desempacotar
# O cara vai passar vários parâmetros, e nós vamos jogar dentro de num

# Retorna todos os valores em uma TUPLA

# def contador(* num):
#     print(num)


# contador(1, 2, 3)
# contador(4, 5, 6, 7, 8)
# contador(9, 10, 11, 12, 13, 14, 15)


# SAÍDA:
# (1, 2, 3)
# (4, 5, 6, 7, 8)
# (9, 10, 11, 12, 13, 14, 15)

def contador(*num):
    for i in num:
        print(i, end=" ")
    print("FIM!")


contador(1, 2, 3)
contador(4, 5, 6, 7, 8)
contador(9, 10, 11, 12, 13, 14, 15)


def tamanho(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")


print()
tamanho(1, 2, 3)
tamanho(4, 5, 6, 7, 8)
tamanho(9, 10, 11, 12, 13, 14, 15)

# Vamos supor que queremos dobrar os valores de uma lista

print()
valores = [7, 2, 5, 0, 4]
print(valores)


# ou poder ser def dobra(lista)
# def dobra(*lista):
#     listaDobrada = []
#     for i in lista:
#         for j in i:
#             listaDobrada.append(j * 2)
#     return listaDobrada

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


def soma(*valores):
    s = 0
    for numeros in valores:
        s += numeros
    print(f"Somando os valores {valores} temos {s}")


dobra(valores)
print(valores)

print()
soma(5, 2)
soma(2, 8, 2)
