from random import randint
from time import sleep as sono

resultados = {}

for i in range(1, 5):
    num = randint(1, 6)
    if num == 1:
        num = "1 ⚀"
    elif num == 2:
        num = "2 ⚁"
    elif num == 3:
        num = "3 ⚂"
    elif num == 4:
        num = "4 ⚃"
    elif num == 5:
        num = "5 ⚄"
    else:
        num = "6 ⚅"
    resultados[f"Jogador {i}"] = num

print("Valores Sorteados 🍀")
for jogador, numero in resultados.items():
    sono(1)
    print(f"    O {jogador} tirou {numero}")
sono(1)

print("Ranking dos Jogadores 🥇")
valores = list(resultados.values())
valores.sort(reverse=True)

cont = 1
list(resultados.keys())
resultadosTemp = resultados.copy()

for i in range(0, 4):
    for jogador, numero in resultadosTemp.items():
        if numero == valores[i]:
            print(f"    {cont}° lugar: {jogador} com {numero}")
            del resultadosTemp[jogador]
            cont += 1
            break
