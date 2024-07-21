n = cont = s = 0

# Laço de Repetição correto com o uso de Quebra
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    cont += 1
print(f"A soma dos {cont} vale {s}")

# print("A soma dos {} valores vale {}".format(cont, s))

# Laço de Repetição errado
"""
while n != 999:
    n = int(input("Digite um número: "))
    cont += 1
    s += n
print(f"A soma vale {s}")
"""
