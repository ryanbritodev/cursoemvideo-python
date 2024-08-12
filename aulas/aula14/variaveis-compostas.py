# VARIÁVEIS COMPOSTAS
# Listas podem armazenar vários valores e são mutáveis
# Tuplas podem armazenar vários valores e são imutáveis
# dados = list()
# dados.append('Pedro')
# dados.append(25)
# print(dados[0])
# Resultado: Pedro
# print(dados[1])
# Resultado: 25
# Os índices representam a posição dos elementos na lista
# pessoas = list()
# pessoas.append(dados[:])
# Aqui, damos o append na estrutura de dados (lista de pessoas)
# Criamos assim, uma lista de listas

dados = list()
dados.append('Pedro')
dados.append(25)
pessoas = list()
pessoas.append(dados[:])
print(pessoas)
dados.append(["Maria", 19])
dados.append(["João", 32])
pessoas.append(dados[3])
pessoas.append(dados[2])
print(pessoas)
print(pessoas[0][0]) # Indice 0 da lista 0
print(pessoas[1][1]) # Indice 1 da lista 1
print(pessoas[2][0]) # Indice 0 da lista 2
print(pessoas[1]) # Lista 1
