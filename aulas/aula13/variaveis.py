a = [2, 3, 4, 7]
# b = a
b = a[:]
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")

# A partir do momento que criamos uma
# alteração em uma lista, o Python cria
# uma ligação entre elas, ou seja, mesmo
# que alternemos o valor de uma lista, em
# uma parte específica do código, ela irá
# alterar por inteiro
