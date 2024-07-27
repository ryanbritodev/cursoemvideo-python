# Utilização de Tuplas

# Tipos de variáveis compostas
# () [] {}
# tupla, lista e dicionário

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

# Tuplas são imutáveis
# lanche[3] = "Sorvete"
# print(lanche[3])
# Esse comando não irá funcionar, já que tuplas não suportam mutação de seus itens!

print(lanche)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-1])
print(lanche[-3:])

print(len(lanche))

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print("Comi pra caramba!")

# ou

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("Comi pra caramba!")

# Dado e a Posição dele
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("Comi pra caramba!")

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)

# A ordem da soma altera a disposição do elementos da tupla
c = a + b
print(c)
c = b + a
print(c)


print(len(c))
print(c.count(5))
print(c.count(4))
print(c.count(9))

# Em que posição está o elemento
print(c.index(8))
print(c.index(4))
# Primeira ocorrência do número
print(c.index(2))
print(c.index(5))
# Primeira ocorrência a partir do índice
print(c.index(5, 1))
print(c.index(2, 4))

# Dentro de Python nós podemos guardar dados ed diferentes tipos dentro de uma tupla (diferentemente de Java)
pessoa = ("Gustavo", 39, "M", 99.88)
# Deleta a variável ou tupla
# del(pessoa[0]) não é possível devido a sua natureza imutável
# del(pessoa)
print(pessoa)
