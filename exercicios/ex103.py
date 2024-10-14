def ficha(nome="<desconhecido>", gols=0):
    if nome.strip().title() == "":
        nome = "<desconhecido>"
    if gols < 0:
        gols = 0
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


print("-" * 30)
jogador = str(input("Nome do Jogador: ")).strip().title()
golsJogador = int(input("Número de Gols: "))
print(ficha(jogador, golsJogador))
