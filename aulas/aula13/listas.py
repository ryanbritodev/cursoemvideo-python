# Listas em Python

# Quando falamos de lista, diferentemente das tuplas, elas são
# representadas por chaves []

# LISTAS SÃO MUTÁVEIS

# Como podemos adicionar elementos a nossa lista em Python?
# Utilizamos o método APPEND (adicionamos ao fim da lista)

# Exemplo:
lanche = ["Hamburguer", "Suco", "Pizza", "Picolé"]
lanche.append("Biscoito")
print(lanche)

# Podemos também definir um local para a inserção do nosso item
# Para isso, podemos utilizar o método INSERT

# Exemplo
lanche.insert(0, "Cachorro Quente")
print(lanche)

# Nós podemos também apagar elementos de uma lista, usando o comando DEL
# Exemplo

del lanche[3]
print(lanche)

# Outro método com função parecida é o método POP (.pop)
# Normalmente, ele é utilizado para apagar o último item da lista,
# porém, nós podemos utilizá-lo para apagar certos índices

lanche.pop(1)
print(lanche)

# Outro método que nós podemos utilizar é o REMOVE (.remove)
# onde nós podemos escolher o elemento que deve ser apagado
# da lista (indicado seu conteúdo)

lanche.remove("Suco")
print(lanche)

# Caso o elemento não esteja na lista, o interpretador de Python
# irá indicar ERRO DE SINTAXE

# Para evitar isso de acontecer, podemos utilizar uma condicional,
# como IF para eliminar o elemento desejado

if "Suco" in lanche:
    lanche.remove("Suco")

# Removendo o último elemento da lista
lanche.pop()
print(lanche)

# Criar uma lista com valores
valores = list(range(1, 11))
print(valores)

valoresEmbaralhados = [8, 2, 5, 4, 9, 3, 0]
valoresEmbaralhados.sort()
print(valoresEmbaralhados)
valoresEmbaralhados.sort(reverse=True)
print(valoresEmbaralhados)
print(len(valoresEmbaralhados))
 