print(""" _____     _             _       _ 
|  ___|_ _| |_ ___  _ __(_) __ _| |
| |_ / _` | __/ _ \| '__| |/ _` | |
|  _| (_| | || (_) | |  | | (_| | |
|_|  \__,_|\__\___/|_|  |_|\__,_|_|""")

numero = int(input("\nDigite um número para ver seu fatorial: "))
numeroOriginal = numero
tot = 1

while numero > 1:
    tot = tot * numero
    numero -= 1

print("\nO fatorial de {} é {}!".format(numeroOriginal, tot))
