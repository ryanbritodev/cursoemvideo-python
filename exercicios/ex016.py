from math import trunc
# O método trunc vem de truncate, ele "corta" os números depois do ponto

numero = float(input("Digite um número real qualquer (ex: 6.317): "))
print("O valor digitado foi {} e sua porção inteira é {}".format(numero, trunc(numero)))

'''num = float(input("Digite um valor: "))
print("O valor digitado foi {} e sua porção inteira é {}".format(num, int(num)))'''
