# Variáveis Compostas em Python (Tuplas)

# lanche =

# Vamos imaginar que temos uma variável chamada "lanche"
# Quando ela é declarada, ela vira um espaço na memória
# Quando queremos fazer uma atribuição, nós podemos utilizar
# o símbolo de "=", criando assim um espaço na memória

# lanche = hamburguer
# lanche RECEBE hamburguer

# O espaço na memória fica preenchido com o hamburguer

# lanche = suco

# Nesse momento, o espaço da memória que estava preenchido com "hamburguer"
# é substituído pelo suco, eliminando o hamburguer

# Desse modo, não podemos ter o lanche com suco e hamburguer devido a limitação
# de um espaço na memória

# Se quisermos criar uma variável que tenha mais espaços na memória, onde consequentemente
# caberão mais tipos de "lanches", como o suco, pizza e até um pudim, devemos utilizar as TUPLAS!

# Elas são variáveis compostas, que possuem múltiplos espaços na memória
# Temos como exemplo de variáveis compostas em Python, tuplas, listas e dicionários

# lanche = hamburguer, suco, pizza, pudim
#              0         1     2      3

# Os elementos de uma tupla podem ser acessados através de índices

# print(lanche[2])
# resultado = pizza

# print(lanche[0:2])
# resultado = hamburger, suco
# (Pizza é omitida)

# print(lanche[1:])
# resultado = suco, pizza, pudim

# print(lanche[-1])
# resultado = pudim
# Sempre pega último elemento

# len(lanche)
# resultado = 4

# for comida in lanche:
#   print(comida)
# O laço for cria uma variável simples chamada "comida", criando um espaço na memória
# que é substuído por diversas vezes pelo valor atual do índice da tupla

# AS TUPLAS SÃO IMUTÁVEIS

# Se por acaso você não gosta de pudim e quer trocar por sorvete,
# essa mudança infelizmente não é possível dentro do Python
