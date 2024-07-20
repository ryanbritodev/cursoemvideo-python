from math import factorial

print(""" _____     _             _       _ 
|  ___|_ _| |_ ___  _ __(_) __ _| |
| |_ / _` | __/ _ \| '__| |/ _` | |
|  _| (_| | || (_) | |  | | (_| | |
|_|  \__,_|\__\___/|_|  |_|\__,_|_|""")

numero = int(input("\nDigite um número para ver seu fatorial: "))
numeroOriginal = numero
tot = 1

print("\nCalculando {}! = ".format(numero), end="")

while numero > 0:
    tot *= numero
    print("{}".format(numero), end="")
    print(" x " if numero > 1 else " = ", end="")
    numero -= 1
print("{}".format(factorial(numeroOriginal)))
print("\nO fatorial de {}! é {}".format(numeroOriginal, factorial(numeroOriginal)))
# print("O fatorial de {}! é {}".format(numeroOriginal, tot))
