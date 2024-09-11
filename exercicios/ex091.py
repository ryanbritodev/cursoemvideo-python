from random import randint
from time import sleep
from operator import itemgetter

jogo = {"jogador1": randint(1, 6),
        "jogador2": randint(1, 6),
        "jogador3": randint(1, 6),
        "jogador4": randint(1, 6)}

ranking = dict()

print("Valores Sorteados 🍀")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Retorna uma lista ordenada pelos valores, de forma inversa (maior pro menor)

print("-=" * 30)
print("<< RANKING DOS JOGADORES >>")

for i, v in enumerate(ranking):
    print(f"{i + 1}° lugar: {v[0]} com {v[1]}.")
    sleep(1)

# Sorted é uma função que ordena, aqui ordenamos na posição 1, no caso o valor, e utilizamos esse módulo
# chamado "itemgetter" para realizar essa ordenação, se fosse parte 0, ele botaria na ordem dos jogadores

# resultados = {}
#
# for i in range(1, 5):
#     num = randint(1, 6)
#     if num == 1:
#         num = "1 ⚀"
#     elif num == 2:
#         num = "2 ⚁"
#     elif num == 3:
#         num = "3 ⚂"
#     elif num == 4:
#         num = "4 ⚃"
#     elif num == 5:
#         num = "5 ⚄"
#     else:
#         num = "6 ⚅"
#     resultados[f"Jogador {i}"] = num
#
# print("Valores Sorteados 🍀")
# for jogador, numero in resultados.items():
#     sono(1)
#     print(f"    O {jogador} tirou {numero}")
# sono(1)
#
# print("Ranking dos Jogadores 🥇")
# valores = list(resultados.values())
# valores.sort(reverse=True)
#
# cont = 1
# list(resultados.keys())
# resultadosTemp = resultados.copy()
#
# for i in range(0, 4):
#     for jogador, numero in resultadosTemp.items():
#         if numero == valores[i]:
#             print(f"    {cont}° lugar: {jogador} com {numero}")
#             del resultadosTemp[jogador]
#             cont += 1
#             break



# OUTRA SOLUÇÃO
# from random import randint
# from time import sleep
#
# jogos1 = {}
# c = 1
#
# for cont in range(1, 5):
#     jogada = randint(1, 6)
#     jogos1["jogador" + str(cont)] = jogada
# print('Valores sorteados:')
# for k, v in jogos1.items():
#     print(f'{k} tirou {v} no dado')
#     sleep(1)
# print('-=' * 30)
# print(f'{"== RANKING DOS JOGADORES ==":^30}')
# jogos2 = dict(sorted(jogos1.items(), key=lambda item: item[1], reverse=True))
# for k, v in jogos2.items():
#     print(f'{c}o. lugar: {k} com {v}.')
#     c +=1
#     sleep(1)
